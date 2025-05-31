# JEE Progress Tracker 📚

A comprehensive Python-based progress tracking tool for JEE (Joint Entrance Examination) preparation. Track your study progress across Physics, Chemistry, and Mathematics with detailed analytics and insights.

## Features ✨

- **Complete JEE Syllabus Coverage**: Pre-loaded with full JEE Main & Advanced syllabus
- **Progress Tracking**: Track completion status and confidence levels for each topic
- **Daily Study Logs**: Log daily study sessions with time tracking
- **Test Score Management**: Record and analyze test performance
- **Dashboard View**: Comprehensive overview of your preparation status
- **Study Plan Generation**: Get personalized study recommendations
- **Data Persistence**: All data saved locally in JSON format

## Quick Start 🚀

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jee-progress-tracker.git
cd jee-progress-tracker
```

2. Run the tracker:
```bash
python jee_tracker.py --dashboard
```

### Basic Usage

#### View Dashboard
```bash
python jee_tracker.py --dashboard
```

#### Log Study Session
```bash
python jee_tracker.py --log-study --subject Physics --hours 2.5 --topic "Kinematics"
```

#### Update Topic Progress
```bash
python jee_tracker.py --subject Mathematics --chapter Algebra --topic "Quadratic Equations" --status completed --confidence 8
```

## Usage Examples 📖

### 1. Starting Your Preparation
```bash
# Log your first study session
python jee_tracker.py --log-study --subject Physics --hours 3 --topic "Laws of Motion"

# Update topic status after studying
python jee_tracker.py --subject Physics --chapter Mechanics --topic "Laws of Motion" --status in_progress --confidence 6
```

### 2. Daily Routine
```bash
# Morning: Study Chemistry for 2 hours
python jee_tracker.py --log-study --subject Chemistry --hours 2 --topic "Atomic Structure"

# Evening: Update progress and confidence
python jee_tracker.py --subject Chemistry --chapter "Physical Chemistry" --topic "Atomic Structure" --status completed --confidence 7

# Check dashboard
python jee_tracker.py --dashboard
```

### 3. Test Preparation
```bash
# Before test: Check weak areas
python jee_tracker.py --dashboard

# After test: Log scores (programmatically)
# Use the Python API to add test scores
```

## Syllabus Coverage 📋

### Physics
- **Mechanics**: Kinematics, Laws of Motion, Work Energy Power, Rotational Motion, Gravitation
- **Thermodynamics**: Heat Transfer, Laws of Thermodynamics, Kinetic Theory
- **Waves & Oscillations**: SHM, Wave Motion, Sound Waves
- **Electromagnetism**: Electrostatics, Current Electricity, Magnetic Effects, Electromagnetic Induction, AC Circuits
- **Optics**: Ray Optics, Wave Optics
- **Modern Physics**: Atomic Structure, Nuclear Physics, Dual Nature of Matter

### Chemistry
- **Physical Chemistry**: Atomic Structure, Chemical Bonding, Thermodynamics, Chemical Equilibrium, Ionic Equilibrium, Electrochemistry, Chemical Kinetics
- **Inorganic Chemistry**: Periodic Table, s-Block, p-Block, d-Block, f-Block, Coordination Compounds
- **Organic Chemistry**: Hydrocarbons, Functional Groups, Biomolecules, Polymers, Organic Reactions

### Mathematics
- **Algebra**: Quadratic Equations, Complex Numbers, Sequences & Series, Permutations & Combinations, Binomial Theorem, Matrices & Determinants
- **Coordinate Geometry**: Straight Lines, Circles, Parabola, Ellipse, Hyperbola
- **Calculus**: Limits, Derivatives, Applications of Derivatives, Integrals, Applications of Integrals, Differential Equations
- **Trigonometry**: Ratios & Functions, Identities, Equations, Inverse Functions
- **Vectors & 3D**: Vector Algebra, 3D Geometry
- **Statistics & Probability**: Statistics, Probability

## Data Structure 💾

Your progress is stored in `jee_progress.json` with the following structure:

```json
{
  "subjects": {
    "Physics": {
      "Mechanics": {
        "Kinematics": {
          "status": "completed",
          "confidence": 8,
          "last_studied": "2025-05-31T10:30:00",
          "time_spent": 5.5,
          "notes": "Covered all basic concepts",
          "problems_solved": 25
        }
      }
    }
  },
  "daily_logs": {},
  "study_hours": {},
  "test_scores": []
}
```

## Advanced Usage 🔧

### Using as Python Module

```python
from jee_tracker import JEEProgressTracker

# Create tracker instance
tracker = JEEProgressTracker()

# Log study session
tracker.log_daily_study("Physics", 2.5, ["Kinematics", "Laws of Motion"])

# Update topic progress
tracker.update_topic_progress("Mathematics", "Algebra", "Quadratic Equations", 
                             status="completed", confidence=8, time_spent=3.0)

# Add test score
tracker.add_test_score("JEE Main Mock Test 1", "Physics", 85, 100)

# Get subject progress
progress = tracker.get_subject_progress("Physics")
print(f"Physics completion: {progress['completion_rate']:.1f}%")

# Generate study plan
plan = tracker.generate_study_plan(days_until_exam=90)
```

## Tips for Effective Usage 💡

1. **Daily Logging**: Log your study sessions daily for accurate time tracking
2. **Honest Assessment**: Rate your confidence honestly (1-10 scale)
3. **Regular Updates**: Update topic status as you progress
4. **Use Notes**: Add notes for important concepts or difficulties
5. **Review Dashboard**: Check dashboard weekly to identify weak areas

## Status Definitions 📊

- **not_started**: Haven't begun studying this topic
- **in_progress**: Currently learning/reviewing this topic  
- **completed**: Finished studying, comfortable with basics
- **revision**: Ready for final revision before exam

## Confidence Scale 🎯

Rate your confidence on a scale of 1-10:
- **1-3**: Just started, many doubts
- **4-6**: Basics clear, some concepts unclear
- **7-8**: Good understanding, can solve most problems
- **9-10**: Expert level, can teach others

## Contributing 🤝

Feel free to contribute by:
- Adding new features
- Improving the syllabus structure
- Creating visualization tools
- Writing documentation

## License 📄

This project is open source and available under the MIT License.

## Support 💬

If you find this tool helpful for your JEE preparation, please star the repository and share it with fellow aspirants!

---

**Good luck with your JEE preparation! 🎯**

*"Success is the sum of small efforts repeated day in and day out."*
