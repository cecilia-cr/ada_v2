"""
Database Manager for Life OS (ALPHA)
Handles all SQLite operations for storing Goals, Habits, Journal Entries, and Daily Context.
"""

import aiosqlite
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "data", "life_os.db")


class DatabaseManager:
    """Manages the Life OS SQLite database with async operations."""
    
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
    
    async def initialize(self):
        """Create all tables if they don't exist."""
        async with aiosqlite.connect(self.db_path) as db:
            # User Profile Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS user_profile (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    bio TEXT,
                    preferences TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Goals Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    status TEXT DEFAULT 'active',
                    priority INTEGER DEFAULT 3,
                    due_date DATE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Habits Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    frequency TEXT DEFAULT 'daily',
                    streak INTEGER DEFAULT 0,
                    last_completed DATE,
                    active BOOLEAN DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Journal Entries Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS journal_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL,
                    content TEXT NOT NULL,
                    sentiment TEXT,
                    tags TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Daily Context Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS daily_context (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL UNIQUE,
                    summary TEXT,
                    focus_area TEXT,
                    energy_level INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            await db.commit()
            print(f"[DB] Database initialized at {self.db_path}")
    
    # === GOALS CRUD ===
    async def create_goal(self, title: str, description: str = "", 
                         category: str = "general", due_date: str = None,
                         priority: int = 3) -> int:
        """Create a new goal and return its ID."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                INSERT INTO goals (title, description, category, due_date, priority)
                VALUES (?, ?, ?, ?, ?)
            """, (title, description, category, due_date, priority))
            await db.commit()
            return cursor.lastrowid
    
    async def get_goals(self, status: str = "active") -> List[Dict]:
        """Retrieve all goals with optional status filter."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("""
                SELECT * FROM goals WHERE status = ? ORDER BY priority DESC, created_at DESC
            """, (status,)) as cursor:
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]
    
    async def update_goal(self, goal_id: int, **kwargs) -> bool:
        """Update a goal's fields."""
        if not kwargs:
            return False
        
        set_clause = ", ".join([f"{k} = ?" for k in kwargs.keys()])
        values = list(kwargs.values()) + [goal_id]
        
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(f"""
                UPDATE goals SET {set_clause}, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, values)
            await db.commit()
            return True
    
    async def delete_goal(self, goal_id: int) -> bool:
        """Delete a goal by ID."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
            await db.commit()
            return True
    
    # === HABITS CRUD ===
    async def create_habit(self, name: str, description: str = "", 
                          frequency: str = "daily") -> int:
        """Create a new habit and return its ID."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                INSERT INTO habits (name, description, frequency)
                VALUES (?, ?, ?)
            """, (name, description, frequency))
            await db.commit()
            return cursor.lastrowid
    
    async def get_habits(self, active_only: bool = True) -> List[Dict]:
        """Retrieve all habits."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            query = "SELECT * FROM habits WHERE active = 1" if active_only else "SELECT * FROM habits"
            async with db.execute(query) as cursor:
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]
    
    async def complete_habit(self, habit_id: int) -> bool:
        """Mark a habit as completed today and update streak."""
        today = datetime.now().date().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            # Get current habit
            async with db.execute("SELECT last_completed, streak FROM habits WHERE id = ?", (habit_id,)) as cursor:
                row = await cursor.fetchone()
                if not row:
                    return False
                
                last_completed, streak = row
                # If completed yesterday, increment streak; else reset
                if last_completed == datetime.now().date().isoformat():
                    # Already completed today
                    return True
                
                # Simple logic: increment streak
                new_streak = streak + 1 if streak else 1
                
                await db.execute("""
                    UPDATE habits SET last_completed = ?, streak = ?
                    WHERE id = ?
                """, (today, new_streak, habit_id))
                await db.commit()
                return True
    
    # === JOURNAL CRUD ===
    async def create_journal_entry(self, content: str, sentiment: str = None, 
                                  tags: str = None) -> int:
        """Create a new journal entry for today."""
        today = datetime.now().date().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                INSERT INTO journal_entries (date, content, sentiment, tags)
                VALUES (?, ?, ?, ?)
            """, (today, content, sentiment, tags))
            await db.commit()
            return cursor.lastrowid
    
    async def get_journal_entries(self, limit: int = 10) -> List[Dict]:
        """Retrieve recent journal entries."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("""
                SELECT * FROM journal_entries ORDER BY date DESC LIMIT ?
            """, (limit,)) as cursor:
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]
    
    # === DAILY CONTEXT ===
    async def set_daily_context(self, summary: str, focus_area: str = None, 
                               energy_level: int = 5) -> bool:
        """Set or update today's context."""
        today = datetime.now().date().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO daily_context (date, summary, focus_area, energy_level)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(date) DO UPDATE SET
                    summary = excluded.summary,
                    focus_area = excluded.focus_area,
                    energy_level = excluded.energy_level
            """, (today, summary, focus_area, energy_level))
            await db.commit()
            return True
    
    async def get_today_context(self) -> Optional[Dict]:
        """Get today's context."""
        today = datetime.now().date().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("SELECT * FROM daily_context WHERE date = ?", (today,)) as cursor:
                row = await cursor.fetchone()
                return dict(row) if row else None
