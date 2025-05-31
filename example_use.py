#!/usr/bin/env python3
"""
Example usage script for JEE Progress Tracker
This script demonstrates various ways to use the tracker
"""

from jee_tracker import JEEProgressTracker
import json

def demo_basic_usage():
    """Demonstrate basic tracking features"""
    print("🚀 JEE Progress Tracker - Demo Usage")
    print("=" * 50)
    
    # Initialize tracker
    tracker = JEEProgressTracker("demo_progress.json")
    
    print("\n1. Logging Study Sessions...")
    # Log some study sessions
    tracker.log_daily_study("Physics", 2.5, ["Kinematics", "Laws of Motion"], 
                           "Covered basic concepts and solved 10 problems")
    tracker.log_daily_study("Chemistry", 2.0, ["Atomic Structure"], 
                           "Studied Bohr model and quantum numbers")
    tracker.log_daily_study("Mathematics", 3.0, ["Quadratic Equations", "Complex Numbers"])
    
    print("✅ Study sessions logged!")
    
    print("\n2. Updating Topic Progress...")
    # Update progress for specific topics
    tracker.update_topic_progress("Physics", "Mechanics", "Kinematics", 
                                 status="completed", confidence=8, problems_solved=15)
    tracker.update_topic_progress("Physics", "Mechanics", "Laws of Motion", 
                                 status="in_progress", confidence=6, problems_solved=8)
    tracker.update_topic_progress("Chemistry", "Physical Chemistry", "Atomic Structure", 
                                 status="completed", confidence=7, problems_solved=12)
    tracker.update_topic_progress("Mathematics", "Algebra", "Quadratic Equations", 
                                 status="in_progress", confidence=5, problems_solved=20)
    
    print("✅ Topic progress updated!")
    
    print("\n3. Adding Test Scores...")
    # Add some test scores
    tracker.add_test_score("Physics Mock Test 1", "Physics", 75, 100)
    tracker.add_test_score("Chemistry Chapter Test", "Chemistry", 88, 100)
    tracker.add_test_score("Math Practice Test", "Mathematics", 65, 100)
    
    print("✅ Test scores added!")
    
    print("\n4. Dashboard Overview:")
    print("-" * 30)
    tracker.display_dashboard()
    
    return tracker

def demo_progress_analysis():
    """Demonstrate progress analysis features"""
    print("\n\n🔍 DETAILED PROGRESS ANALYSIS")
    print("=" * 50)
    
    tracker = JEEProgressTracker("demo_progress.json")
    
    # Analyze each subject
    for subject in ["Physics", "Chemistry", "Mathematics"]:
        print(f"\n📊 {subject} Analysis:")
        progress = tracker.get_subject_progress(subject)
        
        if "error" not in progress:
            print(f"   Total Topics: {progress['total_topics']}")
            print(f"   Completed: {progress['completed_topics']}")
            print(f"   In Progress: {progress['in_progress_topics']}")
            print(f"   Completion Rate: {progress['completion_rate']:.1f}%")
            print(f"   Average Confidence: {progress['avg_confidence']:.1f}/10")
            print(f"   Total Study Time: {progress['total_study_time']:.1f} hours")
            
            print(f"   Chapter-wise Progress:")
            for chapter, data in progress['chapter_progress'].items():
                print(f"     • {chapter}: {data['completion_rate']:.0f}% complete, "
                      f"Confidence: {data['avg_confidence']:.1f}/10")

def demo_study_plan():
    """Demonstrate study plan generation"""
    print("\n\n📅 STUDY PLAN GENERATION")
    print("=" * 50)
    
    tracker = JEEProgressTracker("demo_progress.json")
    
    # Generate study plan
    study_plan = tracker.generate_study_plan(days_until_exam=60)
    
    print(f"\n🎯 Priority Topics (Top 10):")
    for i, topic in enumerate(study_plan['priority_topics'][:10], 1):
        print(f"{i:2d}. {topic['subject']} > {topic['chapter']} > {topic['topic']}")
        print(f"     Priority: {topic['priority']}/10, Current Confidence: {topic['confidence']}/10")

def create_sample_data():
    """Create sample data for demonstration"""
    print("\n\n📝 CREATING COMPREHENSIVE SAMPLE DATA")
    print("=" * 50)
    
    tracker = JEEProgressTracker("sample_progress.json")
    
    # Sample study sessions over multiple days
    study_sessions = [
        ("Physics", 3.0, ["Kinematics"], "2025-05-25"),
        ("Chemistry", 2.5, ["Atomic Structure"], "2025-05-25"),
        ("Mathematics", 2.0, ["Quadratic Equations"], "2025-05-25"),
        ("Physics", 2.0, ["Laws of Motion"], "2025-05-26"),
        ("Chemistry", 3.0, ["Chemical Bonding"], "2025-05-26"),
        ("Mathematics", 2.5, ["Complex Numbers"], "2025-05-26"),
        ("Physics", 1.5, ["Work Energy Power"], "2025-05-27"),
        ("Chemistry", 2.0, ["Thermodynamics"], "2025-05-27"),
        ("Mathematics", 3.0, ["Sequences & Series"], "2025-05-27"),
    ]
    
    for subject, hours, topics, date in study_sessions:
        tracker.log_daily_study(subject, hours, topics, f"Study session on {date}")
    
    # Update topic progress
    topic_updates = [
        ("Physics", "Mechanics", "Kinematics", "completed", 8),
        ("Physics", "Mechanics", "Laws of Motion", "in_progress", 6),
        ("Physics", "Mechanics", "Work Energy Power", "in_progress", 4),
        ("Chemistry", "Physical Chemistry", "Atomic Structure", "completed", 9),
        ("Chemistry", "Physical Chemistry", "Chemical Bonding", "in_progress", 7),
        ("Chemistry", "Physical Chemistry", "Thermodynamics", "in_progress", 5),
        ("Mathematics", "Algebra", "Quadratic Equations", "completed", 7),
        ("Mathematics", "Algebra", "Complex Numbers", "in_progress", 6),
        ("Mathematics", "Algebra", "Sequences & Series", "in_progress", 4),
    ]
    
    for subject, chapter, topic, status, confidence in topic_updates:
        tracker.update_topic_progress(subject, chapter, topic, 
                                     status=status, confidence=confidence, 
                                     problems_solved=15)
    
    # Add test scores
    test_scores = [
        ("Physics Mock Test 1", "Physics", 78, 100, "2025-05-28"),
        ("Chemistry Unit Test", "Chemistry", 85, 100, "2025-05-29"),
        ("Math Weekly Test", "Mathematics", 72, 100, "2025-05-30"),
        ("Full JEE Mock Test", "Physics", 82, 100, "2025-05-31"),
        ("Full JEE Mock Test", "Chemistry", 79, 100, "2025-05-31"),
        ("Full JEE Mock Test", "Mathematics", 68, 100, "2025-05-31"),
    ]
    
    for test_name, subject, score, max_score, date in test_scores:
        tracker.add_test_score(test_name, subject, score, max_score, date)
    
    print("✅ Sample data created in 'sample_progress.json'")
    print("\nRun the following to see the sample dashboard:")
    print("python example_usage.py --sample-dashboard")
    
    return tracker

def show_sample_dashboard():
    """Show dashboard with sample data"""
    try:
        tracker = JEEProgressTracker("sample_progress.json")
        print("\n🎯 SAMPLE DASHBOARD")
        print("=" * 50)
        tracker.display_dashboard()
        
        print("\n📈 DETAILED ANALYSIS")
        print("=" * 30)
        demo_progress_analysis_for_tracker(tracker)
        
    except FileNotFoundError:
        print("❌ Sample data not found. Run: python example_usage.py --create-sample")

def demo_progress_analysis_for_tracker(tracker):
    """Run progress analysis for given tracker"""
    for subject in ["Physics", "Chemistry", "Mathematics"]:
        progress = tracker.get_subject_progress(subject)
        if "error" not in progress and progress['total_topics'] > 0:
            print(f"\n📊 {subject}:")
            print(f"   Completion: {progress['completion_rate']:.1f}%")
            print(f"   Confidence: {progress['avg_confidence']:.1f}/10")
            print(f"   Study Time: {progress['total_study_time']:.1f} hours")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--create-sample":
            create_sample_data()
        elif sys.argv[1] == "--sample-dashboard":
            show_sample_dashboard()
        elif sys.argv[1] == "--demo":
            demo_basic_usage()
            demo_progress_analysis()
            demo_study_plan()
        else:
            print("Usage:")
            print("  python example_usage.py --demo           # Run full demo")
            print("  python example_usage.py --create-sample  # Create sample data")
            print("  python example_usage.py --sample-dashboard # Show
