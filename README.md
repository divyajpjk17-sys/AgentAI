Nova AI
A voice-driven AI assistant for automating everyday digital tasks through natural language commands.

Nova AI is an intelligent assistant that allows users to interact with the application through a voice-based interface. User commands are processed and routed to dedicated modules such as YouTube and Gmail based on pattern matching.

Features
Voice-based interaction through a microphone interface
Natural language command processing
Pattern matching for identifying user intent
YouTube command handling
Video generation functionality
Gmail content generation
Gmail writing functionality
Modular and extensible architecture
WSGI-based application entry point

nova-ai/
│
├── __init__.py
├── wsgi.py
├── requirements.txt
│
├── youtube/
│   ├── __init__.py
│   └── play.py
│
└── gmail/
    ├── __init__.py
    ├── gmail_gen.py
    └── gmail_write.py

Application Flow
User
 |
 | Voice Command
 v
Microphone Interface
 |
 v
Command Processing
 |
 v
Pattern Matching
 |
 +-------------------+
 |                   |
 v                   v
YouTube             Gmail
 |                   |
 v                   v
Video Operations    Email Operations

This project is developed for educational and development purposes.
