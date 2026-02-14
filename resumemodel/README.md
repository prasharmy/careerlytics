# AI Resume Analyzer Package

A comprehensive AI-powered resume analysis and rating system built with Django.

## 📁 Package Structure

```
resumemodel/
├── __init__.py                 # Package initialization
├── README.md                   # This file
├── models_resume.py            # Resume database models
├── resume_analyzer.py          # AI analysis engine
├── views_resume.py             # Django views for resume functionality
├── urls_resume.py              # URL patterns for resume features
├── upload_resume.html          # Resume upload template
├── resume_results.html         # Analysis results template
├── my_resumes.html            # Resume management template
└── requirements_resume.txt     # Package dependencies
```

## 🚀 Features

### 🧠 AI Analysis Engine
- **Multi-Powered Analysis**: Rule-based + NLP + Machine Learning
- **5-Category Scoring**: Skills, Experience, Education, Format, Keywords
- **Intelligent Feedback**: Personalized recommendations
- **Confidence Scoring**: AI confidence metrics

### 📊 Scoring System
- **Overall Score**: 0-100 rating with weighted calculations
- **Category Breakdown**: Detailed scores for each section
- **Performance Metrics**: Processing time and confidence levels
- **Actionable Insights**: Specific improvement suggestions

### 🗄️ Database Models
- **Resume**: File storage and metadata
- **ResumeRating**: Detailed analysis results
- **ResumeKeyword**: Configurable keyword weights
- **ResumeAnalysisLog**: Audit trail and debugging

### 🎨 User Interface
- **Modern Design**: Responsive with dark mode support
- **Drag-and-Drop**: Easy file upload
- **Real-time Progress**: Upload and analysis tracking
- **Visual Feedback**: Color-coded scores and status

## 🔧 Installation

1. **Install Dependencies:**
   ```bash
   pip install -r requirements_resume.txt
   ```

2. **Add to Django Settings:**
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'users',
   ]
   ```

3. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Include URLs:**
   ```python
   # In main urls.py
   path('users/', include('users.urls')),
   ```

## 📡 API Endpoints

```
/users/my-resumes/             # View all resumes
/users/resume-results/<id>/     # View analysis results
/users/download-resume/<id>/     # Download resume file
/users/delete-resume/<id>/       # Delete resume
/users/analyze-resume-api/       # API endpoint for analysis
```

## 🎯 Usage Example

### Student Workflow:
1. Login to student dashboard
2. Navigate to resume upload page
3. Upload PDF or DOCX file (max 5MB)
4. Wait for AI analysis (progress tracking)
5. View detailed results and recommendations
6. Implement suggested improvements
7. Re-upload to track progress

### Analysis Categories:
- **Skills (25%)**: Technical and soft skills relevance
- **Experience (30%)**: Quality and achievements
- **Education (20%)**: Degrees and institutions
- **Format (15%)**: Professional structure
- **Keywords (10%)**: ATS optimization

## 🤖 AI Capabilities

### Text Processing:
- **PDF Extraction**: PyPDF2 + pdfplumber
- **DOCX Processing**: python-docx
- **NLP Analysis**: NLTK tokenization and processing
- **ML Scoring**: scikit-learn TF-IDF similarity

### Smart Analysis:
- **50+ Technical Skills**: Programming, databases, cloud, etc.
- **10+ Soft Skills**: Communication, leadership, teamwork
- **Experience Parsing**: Years, action verbs, achievements
- **Format Validation**: Structure, sections, contact info
- **Keyword Optimization**: ATS-friendly recommendations

## 📈 Performance Metrics

### Analysis Results:
- **Overall Score**: Weighted calculation (0-100)
- **Category Scores**: Individual section ratings
- **Processing Time**: Analysis duration
- **Confidence Score**: AI confidence level (0-1)
- **Recommendations**: Actionable improvement steps

### Audit Trail:
- **Analysis Logs**: Complete audit trail
- **Error Tracking**: Detailed error messages
- **Performance Data**: Processing statistics
- **User Analytics**: Usage patterns and trends

## 🔒 Security Features

- **File Validation**: Type and size restrictions
- **CSRF Protection**: Form security
- **User Authentication**: Login requirements
- **Error Handling**: Comprehensive error management
- **Data Privacy**: Secure file storage

## 🌟 Benefits

### For Students:
- **Instant Feedback**: Immediate resume analysis
- **Professional Guidance**: AI-powered recommendations
- **Progress Tracking**: Improvement over time
- **ATS Optimization**: Better job application success

### For Placement Cells:
- **Quality Control**: Standardized resume evaluation
- **Efficiency**: Automated analysis saves time
- **Analytics**: Student progress tracking
- **Reporting**: Comprehensive statistics

## 🔄 Future Enhancements

- **Advanced ML**: Transformer-based analysis
- **Industry-Specific**: Tailored scoring models
- **Batch Processing**: Multiple resume analysis
- **Mobile App**: Native mobile experience
- **ATS Integration**: Direct employer submissions

## 📞 Support

For technical support or questions about the AI Resume Analyzer package, please refer to the main project documentation or contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: February 2026  
**Framework**: Django 4.0+  
**Python**: 3.8+
