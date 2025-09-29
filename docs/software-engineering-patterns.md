# Software Engineering Patterns & Fundamentals

## Table of Contents

- [Software Engineering Patterns \& Fundamentals](#software-engineering-patterns--fundamentals)
  - [Table of Contents](#table-of-contents)
  - [10 Essential Tasks in Building Applications](#10-essential-tasks-in-building-applications)
  - [1. Data Ingestion](#1-data-ingestion)
  - [2. Data Storage \& Retrieval](#2-data-storage--retrieval)
  - [3. API Calls](#3-api-calls)
  - [4. Data Validation](#4-data-validation)
  - [5. Data Processing](#5-data-processing)
  - [6. User Input Handling](#6-user-input-handling)
  - [7. Business Logic Implementation](#7-business-logic-implementation)
  - [8. Error Handling \& Logging](#8-error-handling--logging)
  - [9. Configuration Management](#9-configuration-management)
  - [10. Code Organization \& Reusability](#10-code-organization--reusability)
  - [Key Insight](#key-insight)
  - [Real-World Example: Building a User Management System](#real-world-example-building-a-user-management-system)
    - [Service Layer Architecture](#service-layer-architecture)
    - [API Integration Pattern](#api-integration-pattern)

---

## 10 Essential Tasks in Building Applications

Each activity below shows which Python concepts you need to master for that task.

---

## 1. Data Ingestion
*Getting data into your application*

**Software Engineering Pattern:** Data Pipeline & ETL (Extract, Transform, Load)

- **Functions** - Create reusable data fetching logic
- **Try/Except** - Handle network errors, invalid data
- **Dictionaries** - Store API responses, configuration
- **Lists** - Collect multiple data items

## 2. Data Storage & Retrieval
*Saving and loading data*

**Software Engineering Pattern:** Data Persistence Layer (CRUD Operations)

- **Dictionaries** - Store structured data (user profiles, settings)
- **Lists** - Store ordered data (logs, transactions)
- **File Operations** - Read/write files, databases
- **JSON** - Standard data format for APIs

## 3. API Calls
*Communicating with external services*

**Software Engineering Pattern:** API Integration & External Services

- **Functions** - Encapsulate API logic
- **Try/Except** - Handle network failures, timeouts
- **Dictionaries** - Structure request/response data
- **String Operations** - Format URLs, headers

## 4. Data Validation
*Checking if data is correct*

**Software Engineering Pattern:** Input Validation & Sanitization

- **If/Else** - Validate conditions
- **Functions** - Reusable validation logic
- **Try/Except** - Handle validation errors
- **String Operations** - Check formats, lengths

## 5. Data Processing
*Transforming and analyzing data*

**Software Engineering Pattern:** Business Logic & Domain Processing

- **For Loops** - Process each item in a dataset
- **Functions** - Break down complex processing
- **Lists/Dictionaries** - Store intermediate results
- **List Comprehensions** - Transform data efficiently

## 6. User Input Handling
*Getting and processing user data*

**Software Engineering Pattern:** User Interface & Input Processing

- **String Operations** - Clean and format input
- **If/Else** - Validate user choices
- **Try/Except** - Handle invalid input gracefully
- **Functions** - Organize input processing logic

## 7. Business Logic Implementation
*Core application rules and workflows*

**Software Engineering Pattern:** Domain Logic & Business Rules

- **Functions** - Implement business rules
- **If/Else** - Make decisions based on conditions
- **Dictionaries** - Store business rules, configurations
- **For Loops** - Apply rules to multiple items

## 8. Error Handling & Logging
*Managing problems and tracking events*

**Software Engineering Pattern:** Error Handling & Observability

- **Try/Except** - Catch and handle errors
- **Functions** - Centralize error handling
- **File Operations** - Write error logs
- **String Operations** - Format error messages

## 9. Configuration Management
*Managing app settings and environment*

**Software Engineering Pattern:** Configuration Management & Environment Control

- **Dictionaries** - Store configuration settings
- **Functions** - Load/save configuration
- **File Operations** - Read config files
- **If/Else** - Handle missing configurations

## 10. Code Organization & Reusability
*Making code maintainable and reusable*

**Software Engineering Pattern:** Code Architecture & Modularity

- **Functions** - Break code into reusable pieces
- **Main Pattern** - Separate executable code from importable code
- **Dictionaries** - Organize related data
- **Try/Except** - Make functions robust

---

## Key Insight

Most applications combine these activities. For example, a web scraper might: ingest data (1) → validate it (4) → process it (5) → store it (2) → handle errors throughout (8).

---

## Real-World Example: Building a User Management System

**Scenario:** You need to build a system that manages user accounts. Here's how the concepts work together:

### Service Layer Architecture

```python
# Domain Model (Dictionary-based entity)
class UserService:
    def __init__(self, config):
        self.config = config  # Configuration management
        self.users = []       # In-memory persistence (replace with DB)
    
    # Service method with proper error handling
    def create_user(self, user_data):
        try:
            # Input validation & sanitization
            if not self._validate_user_data(user_data):
                raise ValueError("Invalid user data")
            
            # Business logic
            user = self._process_user_creation(user_data)
            
            # Data persistence
            self._persist_user(user)
            
            return {"status": "success", "user": user}
            
        except Exception as e:
            # Error handling & observability
            self._log_error("User creation failed", str(e))
            return {"status": "error", "message": str(e)}
    
    # Validation middleware
    def _validate_user_data(self, data):
        if not isinstance(data, dict):
            return False
        if "@" not in data.get("email", ""):
            return False
        if len(data.get("name", "")) < 2:
            return False
        return True
    
    # Business logic processing
    def _process_user_creation(self, data):
        user = {
            "id": self._generate_id(),
            "name": data["name"].strip().title(),
            "email": data["email"].lower(),
            "created_at": self._get_timestamp()
        }
        return user
    
    # Data persistence layer
    def _persist_user(self, user):
        self.users.append(user)
        # In production: database.save(user)
    
    # Utility functions
    def _generate_id(self):
        return f"user_{len(self.users) + 1}"
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _log_error(self, message, details):
        print(f"ERROR: {message} - {details}")
        # In production: logger.error(message, extra={"details": details})
```

### API Integration Pattern

```python
# External service integration
def fetch_user_from_external_api(user_id):
    try:
        # Service abstraction
        response = make_api_request(f"/users/{user_id}")
        
        # Response processing
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(f"API returned {response.status_code}")
            
    except requests.RequestException as e:
        # Circuit breaker pattern
        raise ServiceUnavailableError(f"External service unavailable: {e}")
```

**Architecture Pattern:** Service Layer → Validation Middleware → Business Logic → Data Access Layer → External Services. Each layer uses specific Python concepts for production-ready code.