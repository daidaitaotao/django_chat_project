INT = 1
TEXT = 2
BOOL = 3
RESPONSE_TYPES_CHOICE = (
    (INT, 'integer'),
    (TEXT, 'text'),
    (BOOL, 'boolean'),
)

GREETING = "greeting"
INFORMATION = "information"
INVESTIGATION = "investigation"
GENERAL = "general"
QUESTION_TOPIC_CHOICE = (
    (GREETING, GREETING),
    (INFORMATION, INFORMATION),
    (INVESTIGATION, INVESTIGATION),
    (GENERAL, GENERAL),
)
