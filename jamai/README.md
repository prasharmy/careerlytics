# Soft Skills System

A comprehensive soft skills assessment system with voice recording functionality, database storage, and playback capabilities built with Django and modern web technologies.

## Features

### 🎙️ **Recording Features**
- **Soft Skills Assessment**: Record responses for evaluation
- **Tap-to-Speak**: Simple tap and hold or click to record
- **Visual Feedback**: Animated recording indicators and timer
- **Cross-Platform**: Works on desktop and mobile devices
- **Real-time Timer**: Shows recording duration in MM:SS format

### 💾 **Storage Features**
- **Database Storage**: Recordings stored in Django database
- **File Management**: Automatic file organization and naming
- **Metadata Tracking**: Duration, file size, and timestamp
- **User Association**: Each recording linked to authenticated user

### 🎧 **Playback Features**
- **Built-in Audio Player**: Native HTML5 audio controls
- **Instant Playback**: Listen to recordings immediately
- **Download Support**: Users can download their recordings
- **Delete Functionality**: Remove unwanted recordings

### 🎨 **UI/UX Features**
- **Modern Design**: Beautiful gradient backgrounds and animations
- **Responsive Layout**: Works on all screen sizes
- **Dark Mode Support**: Consistent with existing theme
- **Smooth Animations**: Professional transitions and effects

## Technology Stack

### Backend
- **Django 6.0**: Web framework
- **SQLite**: Database (configurable for production)
- **Media Files**: File storage system

### Frontend
- **HTML5**: Modern semantic markup
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript ES6+**: Modern browser APIs
- **Font Awesome**: Icon library
- **Web Audio API**: Browser recording capabilities

## File Structure

```
softskills/
├── models.py                 # Database models
├── views.py                  # Django views
├── urls.py                   # URL routing
├── apps.py                   # Django app config
├── migrations/
│   └── 0001_initial.py      # Database migrations
└── templates/
    └── softskills/
        └── softskills.html  # Main template
```

## Installation & Setup

### 1. Add App to Django Settings

Add `'softskills'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'softskills',
]
```

### 2. Configure Media Files

Ensure media files are configured in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 3. Update URLs

The soft skills URLs are automatically included in the main `urls.py`.

### 4. Run Migrations

```bash
python manage.py makemigrations softskills
python manage.py migrate
```

### 5. Create Media Directory

```bash
mkdir -p media/voice_recordings
```

## Usage

### Access the Voice Recording System

Navigate to: `http://127.0.0.1:8000/voice-recording/`

### Recording Process

1. **Start Recording**: Tap/click the microphone button
2. **Recording**: Visual feedback shows recording status and timer
3. **Stop Recording**: Release the button or click again
4. **Save**: Recording automatically saves to database
5. **Playback**: Use built-in audio controls to listen

### Managing Recordings

- **View**: All recordings listed with metadata
- **Play**: Built-in audio player for each recording
- **Delete**: Remove unwanted recordings with confirmation
- **Download**: Right-click audio player to download

## API Endpoints

### Main Page
- **URL**: `/voice-recording/`
- **Method**: GET
- **Auth**: Required (user must be logged in)

### Save Recording
- **URL**: `/voice-recording/save/`
- **Method**: POST
- **Auth**: Required
- **Data**: Base64 encoded audio, duration, title

### Delete Recording
- **URL**: `/voice-recording/delete/<id>/`
- **Method**: DELETE
- **Auth**: Required

### Get Recordings
- **URL**: `/voice-recording/get-recordings/`
- **Method**: GET
- **Auth**: Required

## Database Schema

### VoiceRecording Model

```python
class VoiceRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='voice_recordings/')
    duration = models.DurationField()
    file_size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## Browser Compatibility

### Supported Browsers
- ✅ Chrome 66+
- ✅ Firefox 60+
- ✅ Safari 11+
- ✅ Edge 79+

### Required Features
- **MediaRecorder API**: For audio recording
- **File API**: For file handling
- **Fetch API**: For AJAX requests
- **ES6 JavaScript**: For modern syntax

## Security Considerations

### Authentication
- All endpoints require user authentication
- Recordings are isolated by user
- CSRF protection enabled

### File Security
- Audio files stored in media directory
- File size validation
- File type restrictions (audio/wav)

### Data Privacy
- Recordings linked to user accounts
- No public access to audio files
- Secure file serving through Django

## Performance Optimization

### Frontend
- Efficient audio blob handling
- Lazy loading of recordings
- Optimized animations with CSS transforms

### Backend
- Database indexing on user and created_at
- Efficient file serving
- Minimal database queries

## Troubleshooting

### Common Issues

**Microphone Permission Denied**
- Check browser permissions
- Ensure HTTPS in production
- Try different browser

**Recording Not Saving**
- Check media directory permissions
- Verify database migrations
- Check browser console for errors

**Audio Playback Issues**
- Verify file format support
- Check browser audio capabilities
- Ensure file exists in media directory

### Debug Mode

Enable debug mode in JavaScript:

```javascript
// In browser console
localStorage.setItem('voice_recording_debug', 'true');
```

## Customization

### Styling
Modify the CSS classes in the template to match your theme:

```css
.voice-button {
    /* Custom button styling */
}

.recording-pulse {
    /* Custom recording animation */
}
```

### Recording Settings
Adjust recording parameters in views.py:

```python
# Modify audio quality settings
mediaRecorder = new MediaRecorder(stream, {
    mimeType: 'audio/webm;codecs=opus'
});
```

## Production Deployment

### Required Settings

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/production/media/'

# Secure file serving
SECURE_SSL_REDIRECT = True
```

### Web Server Configuration

Configure your web server (Nginx/Apache) to serve media files:

```nginx
# Nginx example
location /media/ {
    alias /path/to/production/media/;
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is part of the Careerlytics system and follows the same licensing terms.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review browser console for errors
3. Verify Django logs
4. Test with different browsers

---

**Note**: This voice recording system is designed for educational and professional use. Ensure compliance with local regulations regarding audio recording and privacy.
