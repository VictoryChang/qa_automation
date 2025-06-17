get_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "string"
    },
    "created_time": {
      "type": "integer"
    },
    "is_done": {
      "type": "boolean"
    },
    "task_id": {
      "type": "string"
    },
    "ttl": {
      "type": "integer"
    },
    "user_id": {
      "type": "string"
    }
  },
  "required": [
    "content",
    "created_time",
    "is_done",
    "task_id",
    "ttl",
    "user_id"
  ]
}


post_schema = {
  "type": "object",
  "properties": {
    "task": get_schema
  },
  "required": [
    "task"
  ]
}


put_schema = {
    "type": "object",
    "properties": {
        "updated_task_id": {
            "type": "string"
        }
    },
    "required": [
        "updated_task_id"
    ]
}


list_schema = {
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "items": get_schema
    }
  },
  "required": [
    "tasks"
  ]
}


delete_schema = {
    "type": "object",
    "properties": {
        "deleted_task_id": {
            "type": "string"
        }
    },
    "required": ["deleted_task_id"]
}
