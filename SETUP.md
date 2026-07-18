# MathSolve Pro Setup Guide

> Complete setup and configuration guide for MathSolve Pro v1.0.0

---

## 📋 Prerequisites

- Python 3.7+
- pip (Python package manager)
- GROQ API Key ([Get one free here](https://console.groq.com))
- Modern web browser (Chrome, Firefox, Safari, Edge)

---

## 🚀 Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/deyashok1904-arch/Maths-solver.git
cd Maths-solver
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install flask requests python-dotenv
```

### Step 4: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your GROQ API key
# Use your favorite editor (nano, vim, VS Code, etc.)
nano .env
```

**Edit `.env` file:**
```env
GROQ_API_KEY=gsk_your_real_key_here
PORT=3000
DEBUG=False
```

### Step 5: Run the Server

```bash
python server.py
```

**Expected output:**
```
✅ All validations passed!
 * Serving Flask app 'app'
 * Environment: production
 * Debug mode: off
 * Running on http://127.0.0.1:3000
```

### Step 6: Open in Browser

- Navigate to: `http://localhost:3000`
- Or open `MathSolve_Pro.html` directly

---

## 🔧 Configuration

### Environment Variables Reference

| Variable | Required | Default | Example | Notes |
|----------|----------|---------|---------|-------|
| `GROQ_API_KEY` | ✅ Yes | - | `gsk_...` | Get from [Groq Console](https://console.groq.com) |
| `PORT` | ❌ No | 3000 | 8080 | Any available port |
| `DEBUG` | ❌ No | False | True | Only for development |

### Configuration Examples

**Development Setup:**
```env
GROQ_API_KEY=gsk_your_dev_key
PORT=3000
DEBUG=True
```

**Production Setup:**
```env
GROQ_API_KEY=gsk_your_prod_key
PORT=8080
DEBUG=False
```

**Custom Port:**
```env
GROQ_API_KEY=gsk_your_key
PORT=5000
DEBUG=False
```

---

## 🆘 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "GROQ_API_KEY not set"

**Solution:**
1. Create `.env` file: `cp .env.example .env`
2. Add your API key to `.env`
3. Verify file exists in project root
4. Restart the server

### Issue: "Port 3000 already in use"

**Solution 1 - Use different port:**
```env
PORT=8080
```

**Solution 2 - Kill process using port (macOS/Linux):**
```bash
lsof -ti:3000 | xargs kill -9
```

**Solution 3 - Kill process using port (Windows):**
```bash
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### Issue: "Connection refused" when accessing localhost

**Solution:**
1. Verify server is running
2. Check correct port: `http://localhost:3000`
3. Check .env configuration
4. Restart server

### Issue: "File not found" error

**Solution:**
1. Ensure you're in project root directory
2. Verify `MathSolve_Pro.html` exists
3. Check file permissions

---

## 🐍 Python Version Check

```bash
python --version
# Should be 3.7 or higher
```

If not, install latest Python from [python.org](https://www.python.org)

---

## 📦 Requirements File

**requirements.txt:**
```
Flask==2.3.3
requests==2.31.0
python-dotenv==1.0.0
```

---

## 🔐 Security Checklist

Before deploying to production:

- [ ] Set `DEBUG=False` in `.env`
- [ ] Use a strong GROQ API key
- [ ] Store `.env` securely (never commit to git)
- [ ] Use environment variables from secure secrets manager
- [ ] Enable HTTPS/SSL in production
- [ ] Set appropriate `PORT` (not 3000)
- [ ] Review `.gitignore` is in place

---

## 📁 File Structure

```
Maths-solver/
├── .env                      # Environment variables (create from .env.example)
├── .env.example              # Configuration template
├── .gitignore                # Git exclusion rules
├── CHANGELOG.md              # Version history
├── RELEASE_NOTES.md          # Release information
├── SETUP.md                  # This file
├── server.py                 # Flask server
├── MathSolve_Pro.html        # Main application
└── css/
    └── styles.css            # Extracted styles
```

---

## ✅ Verification

After setup, verify everything works:

1. **Server runs without errors:**
   ```bash
   python server.py
   ```
   Should show: `✅ All validations passed!`

2. **Can access calculator:**
   - Open `http://localhost:3000` or `MathSolve_Pro.html`
   - Should display calculator interface

3. **AI features work:**
   - Click AI Solver tab
   - Should be able to input math problems

---

## 🆘 Getting Help

1. **Check CHANGELOG.md** for recent changes
2. **Review error messages** carefully
3. **Check .env configuration** 
4. **Verify GROQ API key** is valid
5. **Open a GitHub issue** with:
   - Error message
   - Your OS and Python version
   - Steps to reproduce
   - Contents of `.env.example` (NOT `.env`!)

---

## 🎓 Next Steps

Once setup is complete:

1. Explore the calculator features
2. Try the AI Solver
3. Check out different tabs (Algebra, Trigonometry, Calculus, etc.)
4. Read CHANGELOG.md for feature details

---

## 📞 Support

**Issues or Questions?**
- Open an issue on GitHub
- Include your Python version
- Describe the problem clearly
- Share error messages (sanitize sensitive data)

---

**Happy Solving! 🎓📐**
