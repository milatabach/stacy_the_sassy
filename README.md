
# Stacy the Sassy - How to Use a Camera Website

**Stacy the Sassy** is a beginner-friendly website built with Python (Flask) to teach users how to use a camera. It walks through concepts like aperture, ISO, and shutter speed, featuring fun visuals and interactive examples.

---

## Project Structure

- Flask backend to serve HTML templates
- Static folder for images and styles
- Templates for each camera concept page (aperture, ISO, shutter speed, quizzes)

---

## Setup Instructions

1. Clone or download the repository.

2. Install required packages:
   ```bash
   pip install flask
   ```

3. Run the server:
   ```bash
   python server.py
   ```
   (or replace `server.py` if the main file is named differently.)

4. Visit the site:
   Open your browser and go to http://localhost:5000

---

## Requirements

- Python 3.x
- Flask (pip install flask)

---

## Project Purpose

This project was designed to make learning manual camera settings fun and accessible, using simple language, playful design, and easy-to-navigate tutorials.

---

## Page Guide

| File Name | Purpose |
|:---|:---|
| `home.html` | Landing page introducing the project. |
| `camera.html` | Shows some important buttons on the camera, and page to access shutter speed. |
| `back_of_camera.html` | Explains camera menu, and page to access ISO and Aperture. |
| `learning.html`, `learning2.html` | Stacey introduction and introduction to triangle of exposure. |
| Shutter Speed Pages ||
| `shutter.html` | Shutter speed overview. |
| `shutter_def.html` | Important definitions regarding shutter speed. |
| `shutter_opening.html` | Introduction to shutter speed. |
| `shutter_exposure.html` | Shutter speed's impact on exposure. |
| `shutter_motion.html` | How shutter speed affects motion blur. |
| Aperture Pages ||
| `aperture.html` | Aperture basics overview. |
| `aperture_def.html` | Important definitions regardig aperture. |
| `aperture_opening.html` | Introduction to aperture. |
| `aperture2.html`, `aperture3.html` | Further examples and depth of field info. |
| ISO Pages ||
| `iso_opening.html` | Introduction to ISO. |
| `iso_grain.html` | The drawback of high ISO (grain/noise). |
| Quizzes and Games ||
| `mcq_quiz.html` | Multiple choice quiz. |
| `tf_quiz.html` | True/false quiz. |
| `match.html` | Matching game quiz. |
| `quiz_1.html` to `quiz_5.html` | Series of quiz pages where user can adjust a virtual camera with pictures of Stacey. |
| `results.html` | Display quiz results. |
| Stacy Themed Pages ||
| `stacey2.html`, `stacey3.html` | Stacy introduces and explains camera concepts, and triangle of exposure. |
| `stacey_aperture.html` | Stacy introduces aperture. |
| `stacey_shutter.html` | Stacy introduces shutter speed. |
| `stacey_iso.html` | Stacy introduces ISO. |
| `stacey_quiz.html` | Stacy introduces the quiz. |
| Other ||
| `layout.html` | Master template for consistent styling across pages. |

---

## Credits

Created by Stella, Mila, Dom and Lilly for an educational project.
