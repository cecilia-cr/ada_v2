generate_cad_prototype_tool = {
    "name": "generate_cad_prototype",
    "description": "Generates a 3D wireframe prototype based on a user's description. Use this when the user asks to 'visualize', 'prototype', 'create a wireframe', or 'design' something in 3D.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "prompt": {
                "type": "STRING",
                "description": "The user's description of the object to prototype."
            }
        },
        "required": ["prompt"]
    }
}




write_file_tool = {
    "name": "write_file",
    "description": "Writes content to a file at the specified path. Overwrites if exists.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the file to write to."
            },
            "content": {
                "type": "STRING",
                "description": "The content to write to the file."
            }
        },
        "required": ["path", "content"]
    }
}

read_directory_tool = {
    "name": "read_directory",
    "description": "Lists the contents of a directory.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the directory to list."
            }
        },
        "required": ["path"]
    }
}

read_file_tool = {
    "name": "read_file",
    "description": "Reads the content of a file.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the file to read."
            }
        },
        "required": ["path"]
    }
}

# === LIFE OS TOOLS ===
create_goal_tool = {
    "name": "create_goal",
    "description": "Create a new life goal for the user to track. Use this when the user expresses intent to achieve something.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "title": {
                "type": "STRING",
                "description": "The title/name of the goal."
            },
            "description": {
                "type": "STRING",
                "description": "Detailed description of the goal."
            },
            "category": {
                "type": "STRING",
                "description": "Category: 'health', 'career', 'relationships', 'personal', or 'financial'."
            },
            "due_date": {
                "type": "STRING",
                "description": "Optional due date in YYYY-MM-DD format."
            }
        },
        "required": ["title"]
    }
}

view_goals_tool = {
    "name": "view_goals",
    "description": "View all active goals for the user.",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}

create_habit_tool = {
    "name": "create_habit",
    "description": "Create a new habit to track. Use when the user wants to build a new routine.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "name": {
                "type": "STRING",
                "description": "Name of the habit."
            },
            "description": {
                "type": "STRING",
                "description": "Why this habit matters."
            },
            "frequency": {
                "type": "STRING",
                "description": "Frequency: 'daily', 'weekly', or 'custom'."
            }
        },
        "required": ["name"]
    }
}

complete_habit_tool = {
    "name": "complete_habit",
    "description": "Mark a habit as completed for today.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "habit_name": {
                "type": "STRING",
                "description": "The name of the habit to mark complete."
            }
        },
        "required": ["habit_name"]
    }
}

tools_list = [{"function_declarations": [
    generate_cad_prototype_tool,
    write_file_tool,
    read_directory_tool,
    read_file_tool,
    create_goal_tool,
    view_goals_tool,
    create_habit_tool,
    complete_habit_tool
]}]


