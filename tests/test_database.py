
import pytest
import asyncio
import os
import shutil
from backend.database import DatabaseManager

# Use a test database path
TEST_DB_PATH = os.path.join(os.path.dirname(__file__), "test_life_os.db")

@pytest.fixture
async def db():
    # Setup
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    manager = DatabaseManager(db_path=TEST_DB_PATH)
    await manager.initialize()
    
    yield manager
    
    # Teardown
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

@pytest.mark.asyncio
async def test_goals_crud(db):
    # Create
    goal_id = await db.create_goal("Test Goal", "Description", "health")
    assert goal_id is not None
    
    # Read
    goals = await db.get_goals()
    assert len(goals) == 1
    assert goals[0]['title'] == "Test Goal"
    
    # Update
    assert await db.update_goal(goal_id, status="completed")
    goals = await db.get_goals(status="completed")
    assert len(goals) == 1
    
    # Delete
    assert await db.delete_goal(goal_id)
    goals = await db.get_goals(status="completed")
    assert len(goals) == 0

@pytest.mark.asyncio
async def test_habits_crud(db):
    # Create
    habit_id = await db.create_habit("Exercise", "Daily run", "daily")
    assert habit_id is not None
    
    # Read
    habits = await db.get_habits()
    assert len(habits) == 1
    assert habits[0]['name'] == "Exercise"
    
    # Complete
    assert await db.complete_habit(habit_id)
    # Verify streak updated
    habits = await db.get_habits()
    assert habits[0]['streak'] == 1

@pytest.mark.asyncio
async def test_journal(db):
    entry_id = await db.create_journal_entry("Dear Diary", "positive", "test")
    assert entry_id is not None
    
    entries = await db.get_journal_entries()
    assert len(entries) == 1
    assert entries[0]['content'] == "Dear Diary"

@pytest.mark.asyncio
async def test_daily_context(db):
    assert await db.set_daily_context("Busy day", "Coding", 8)
    
    context = await db.get_today_context()
    assert context is not None
    assert context['focus_area'] == "Coding"
    assert context['energy_level'] == 8
