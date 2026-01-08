"""
Context Engine for Life OS (ALPHA)
Aggregates user data to provide daily briefings and intelligent context-aware responses.
"""

from datetime import datetime
from typing import Dict, List, Optional
from database import DatabaseManager


class ContextEngine:
    """Aggregates and queries life data to provide context to ALPHA."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    async def get_daily_briefing(self) -> str:
        """Generate a morning briefing with goals, habits, and context."""
        today = datetime.now().strftime("%A, %B %d, %Y")
        
        # Get active goals
        goals = await self.db.get_goals(status="active")
        
        # Get active habits
        habits = await self.db.get_habits(active_only=True)
        
        # Get today's context
        context = await self.db.get_today_context()
        
        # Build briefing
        briefing = f"**Daily Briefing for {today}**\n\n"
        
        if context:
            briefing += f"**Today's Focus**: {context.get('focus_area', 'Not set')}\n"
            briefing += f"**Energy Level**: {context.get('energy_level', 'N/A')}/10\n\n"
        
        if goals:
            briefing += f"**Active Goals ({len(goals)})**:\n"
            for goal in goals[:5]:  # Top 5
                briefing += f"- {goal['title']} ({goal['category']})\n"
            briefing += "\n"
        else:
            briefing += "**No active goals set.**\n\n"
        
        if habits:
            briefing += f"**Daily Habits ({len(habits)})**:\n"
            for habit in habits:
                status = "✓" if habit.get('last_completed') == datetime.now().date().isoformat() else "☐"
                briefing += f"{status} {habit['name']}\n"
            briefing += "\n"
        else:
            briefing += "**No habits tracked.**\n\n"
        
        return briefing
    
    async def get_goals_summary(self) -> str:
        """Get a text summary of all active goals."""
        goals = await self.db.get_goals(status="active")
        if not goals:
            return "No active goals."
        
        summary = "Your Active Goals:\n"
        for goal in goals:
            summary += f"- {goal['title']}: {goal['description']}\n"
        return summary
    
    async def log_interaction(self, user_input: str, assistant_response: str):
        """Log conversation for future context (can be enhanced with embeddings)."""
        # For now, just store in journal as a summary
        # Future: Store in separate interactions table with embeddings
        pass
    
    async def query_context(self, query: str) -> str:
        """
        Simple context query. In the future, this could use embeddings/RAG.
        For now, it searches journal entries and goals.
        """
        # Placeholder for semantic search
        # For now, return recent journal entries
        entries = await self.db.get_journal_entries(limit=3)
        if not entries:
            return "No context found."
        
        result = "Recent Journal Entries:\n"
        for entry in entries:
            result += f"- {entry['date']}: {entry['content'][:100]}...\n"
        return result
