#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': 'Best scholarships for Masters in USA withuot IELTS and GRE'
  }
  LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
