# Mock Test System for AI Resume Analyzer

A comprehensive testing and debugging environment for the AI Resume Analyzer system.

## 📋 Overview

This Mock Test System provides a complete testing framework for validating and debugging the AI Resume Analyzer application. It includes frontend interface, backend logic, database models, and utility functions for comprehensive testing.

## 🚀 Features

### 🧪 Test Categories
- **Resume Analysis Test**: Tests resume parsing, skill extraction, and scoring functionality
- **AI Model Test**: Validates AI model loading, prediction accuracy, and response times
- **Database Test**: Checks database connectivity, CRUD operations, and performance
- **API Test**: Tests API endpoints, authentication, and error handling
- **Performance Test**: Monitors system performance under load and stress conditions
- **Security Test**: Validates authentication, authorization, and vulnerability protection

### 🎯 Key Features
- **Full-screen Test Execution**: Immersive testing experience with progress indicators
- **Real-time Status Updates**: Live test status and progress tracking
- **Comprehensive Logging**: Detailed logging system for debugging and analysis
- **Test Result Storage**: Persistent storage of test results and metrics
- **Report Generation**: Automated report generation in multiple formats
- **Test Scheduling**: Automated test execution with configurable schedules
- **Health Monitoring**: System health monitoring and performance metrics

## 📁 File Structure

```
d:/matrix/mocktestdata/
├── mock_test.html              # Frontend interface
├── mock_test_backend.py         # Python backend logic
├── mock_test_models.py          # Django models
├── mock_test_views.py           # Django views
├── mock_test_urls.py            # URL routing
├── mock_test_utils.py           # Utility functions
├── README.md                   # Documentation
└── mock_test.db               # SQLite database (created automatically)
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Django 4.0+
- SQLite 3
- Modern web browser with JavaScript support

### Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install django django sqlite3 psutil
   ```

2. **Configure Django Settings**
   Add to your `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ... your existing apps
       'mocktestdata',
   ]
   ```

3. **Update URL Configuration**
   Add to your main `urls.py`:
   ```python
   urlpatterns = [
       # ... your existing URLs
       path('mock-test/', include('mocktestdata.mock_test_urls')),
   ]
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations mocktestdata
   python manage.py migrate
   ```

## 🎮 Usage

### Frontend Interface

Access the mock test interface at:
```
http://127.0.0.1:8000/mocktestdata/mock_test.html
```

### API Endpoints

#### Test Execution
```bash
# Run a specific test
POST /mock-test/run/<test_type>/
Content-Type: application/json

# Example: Run resume analysis test
curl -X POST http://127.0.0.1:8000/mock-test/run/resume_analysis/ \
  -H "Content-Type: application/json" \
  -d '{}'
```

#### Get Test Results
```bash
# Get all test results
GET /mock-test/results/

# Get results for specific test type
GET /mock-test/results/resume_analysis/
```

#### Test Statistics
```bash
# Get comprehensive statistics
GET /mock-test/stats/
```

#### Test Configuration
```bash
# Get configurations
GET /mock-test/config/

# Save configuration
POST /mock-test/config/
Content-Type: application/json

{
  "name": "resume_analysis_config",
  "description": "Configuration for resume analysis tests",
  "configuration": {
    "timeout": 30,
    "retry_count": 3,
    "sample_data": true
  }
}
```

#### Report Generation
```bash
# Generate report
POST /mock-test/generate/
Content-Type: application/json

{
  "report_type": "summary",
  "test_types": ["resume_analysis", "ai_model"]
}
```

### Command Line Interface

Run tests directly from command line:
```bash
cd d:/matrix/mocktestdata/
python mock_test_backend.py
```

## 🧪 Test Categories

### Resume Analysis Test
- **Text Parsing**: Validates resume text extraction and parsing
- **Skill Extraction**: Tests identification and extraction of skills
- **Score Calculation**: Validates resume scoring algorithms
- **Database Storage**: Tests data persistence and retrieval
- **Format Validation**: Checks resume format compliance

### AI Model Test
- **Model Loading**: Validates AI model initialization and loading
- **Prediction Accuracy**: Tests model prediction accuracy and confidence
- **Response Time**: Measures model inference speed
- **Error Handling**: Validates model error handling and recovery
- **Memory Usage**: Monitors model memory consumption

### Database Test
- **Connection Testing**: Validates database connectivity and authentication
- **CRUD Operations**: Tests Create, Read, Update, Delete operations
- **Data Integrity**: Validates data consistency and constraints
- **Performance Metrics**: Measures query performance and optimization
- **Transaction Handling**: Tests transaction management and rollback

### API Test
- **Endpoint Testing**: Validates all API endpoints functionality
- **Authentication**: Tests user authentication and authorization
- **Request Validation**: Validates input validation and sanitization
- **Response Format**: Tests API response structure and format
- **Error Handling**: Validates proper error responses and status codes
- **Rate Limiting**: Tests API rate limiting and throttling

### Performance Test
- **Load Testing**: Simulates high user load and concurrent requests
- **Stress Testing**: Tests system limits and breaking points
- **Response Time**: Measures API and database response times
- **Resource Usage**: Monitors CPU, memory, and disk usage
- **Scalability**: Tests system behavior under increasing load
- **Throughput**: Measures requests per second and system capacity

### Security Test
- **Authentication**: Tests login mechanisms and session management
- **Authorization**: Validates role-based access control
- **Input Validation**: Tests for SQL injection and XSS protection
- **Session Security**: Validates session handling and timeout
- **CSRF Protection**: Tests Cross-Site Request Forgery protection
- **Data Encryption**: Validates sensitive data encryption and storage

## 📊 Test Results

### Result Format
Each test result includes:
- **Status**: success, error, running, pending
- **Message**: Descriptive result message
- **Details**: Array of specific test details
- **Execution Time**: Time taken to complete test (seconds)
- **Metrics**: Additional performance and system metrics
- **Timestamp**: When the test was executed

### Success Criteria
- **Resume Analysis**: All parsing, extraction, and scoring functions work
- **AI Model**: Model loads, predictions are accurate, response time < 2s
- **Database**: Connection successful, CRUD operations work, performance > 80%
- **API**: All endpoints respond correctly, authentication works
- **Performance**: Response time < 1s, system resources < 80%
- **Security**: All vulnerability tests pass, authentication works correctly

## 🔧 Configuration

### Test Configuration Options
- **Timeout Settings**: Configure test execution timeouts
- **Retry Logic**: Set retry attempts and backoff strategies
- **Data Generation**: Configure realistic test data generation
- **Performance Thresholds**: Set acceptable performance limits
- **Security Parameters**: Configure security test parameters

### Environment Variables
```bash
# Test database path
export MOCK_TEST_DB_PATH="/path/to/test.db"

# Test execution timeout
export MOCK_TEST_TIMEOUT=30

# Enable debug logging
export MOCK_TEST_DEBUG=true
```

## 📈 Monitoring & Logging

### Log Levels
- **DEBUG**: Detailed debugging information
- **INFO**: General information about test execution
- **WARNING**: Warning messages for potential issues
- **ERROR**: Error messages for failed tests
- **CRITICAL**: Critical system failures

### Performance Metrics
- **Execution Time**: Time taken for each test
- **Memory Usage**: System memory consumption
- **CPU Usage**: Processor utilization
- **Disk I/O**: Read/write operations and throughput
- **Network I/O**: Network traffic and response times

### Health Checks
- **System Status**: Overall system health indicator
- **Resource Availability**: Database and API availability
- **Performance Trends**: Historical performance data
- **Error Rates**: Test failure and error frequencies

## 🚨 Troubleshooting

### Common Issues

#### Test Execution Failures
- **Database Connection**: Check database configuration and connectivity
- **Import Errors**: Verify Python path and Django settings
- **Permission Issues**: Ensure proper file and directory permissions
- **Port Conflicts**: Check for conflicting services on ports

#### Performance Issues
- **Slow Execution**: Check system resources and background processes
- **Memory Leaks**: Monitor memory usage during long-running tests
- **Database Locks**: Identify and resolve database contention
- **Network Timeouts**: Check network connectivity and firewall settings

#### Frontend Issues
- **JavaScript Errors**: Check browser console for errors
- **CSS Loading**: Verify theme toggle and styling
- **API Calls**: Ensure proper endpoint URLs and authentication
- **Browser Compatibility**: Test in different browsers and versions

### Debug Mode
Enable debug mode for detailed logging:
```bash
export MOCK_TEST_DEBUG=true
python mock_test_backend.py
```

## 🔄 Updates & Maintenance

### Version Control
- Track changes in version control system
- Tag releases with version numbers
- Document breaking changes and migrations

### Regular Maintenance
- Clean up old test data (default: 30 days)
- Update test data and configurations
- Review and optimize test performance
- Update dependencies and security patches

### Backup Strategy
- Regular database backups
- Configuration file backups
- Test result exports and archives
- System state snapshots

## 📚 API Reference

### Response Formats

#### Success Response
```json
{
  "status": "success",
  "message": "Test completed successfully",
  "details": ["Detail 1", "Detail 2"],
  "execution_time": 2.45,
  "metrics": {
    "additional": "data"
  }
}
```

#### Error Response
```json
{
  "status": "error",
  "message": "Test failed: Description of error",
  "details": ["Error detail"],
  "execution_time": 1.23
}
```

### Status Codes
- **200**: Success
- **400**: Bad Request (invalid parameters)
- **401**: Unauthorized (authentication required)
- **403**: Forbidden (insufficient permissions)
- **404**: Not Found (invalid endpoint)
- **500**: Internal Server Error (test execution failed)

## 🎯 Best Practices

### Test Design
- **Isolation**: Tests should not interfere with each other
- **Reproducibility**: Tests should produce consistent results
- **Atomicity**: Tests should be all-or-nothing operations
- **Idempotency**: Multiple identical requests should have same effect

### Performance Optimization
- **Async Operations**: Use asynchronous operations for I/O-bound tasks
- **Connection Pooling**: Reuse database connections efficiently
- **Caching**: Cache frequently accessed data and results
- **Batch Processing**: Process multiple items together when possible

### Security Considerations
- **Input Validation**: Always validate and sanitize inputs
- **Error Handling**: Never expose sensitive information in error messages
- **Authentication**: Use strong authentication mechanisms
- **Authorization**: Implement proper access control
- **Encryption**: Protect sensitive data at rest and in transit

## 📞 Support

### Getting Help
- Check the troubleshooting section for common issues
- Review logs for detailed error information
- Verify configuration and environment setup
- Test with minimal setup to isolate issues

### Contributing
- Follow the existing code style and patterns
- Add comprehensive tests for new features
- Update documentation for any changes
- Use meaningful commit messages

### License
This Mock Test System is part of the AI Resume Analyzer project.
Please refer to the main project license for usage terms.

---

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install django django sqlite3
   ```

2. **Setup Database**
   ```bash
   python manage.py makemigrations mocktestdata
   python manage.py migrate
   ```

3. **Run Tests**
   ```bash
   # Frontend: Open in browser
   http://127.0.0.1:8000/mocktestdata/mock_test.html
   
   # Backend: Command line
   python mock_test_backend.py
   
   # API: REST endpoints
   curl -X POST http://127.0.0.1:8000/mock-test/run/resume_analysis/
   ```

4. **Monitor Results**
   ```bash
   # View results in database
   python manage.py shell
   >>> from mocktestdata.models import MockTestResult
   >>> MockTestResult.objects.all()
   ```

Start testing your AI Resume Analyzer system comprehensively! 🧪✨
