## Description
- It takes video as input and extract different sildes(Images) from the video.
- Then It convert images into PDF.
- It Use structural_similarity to check similarity between two frames.
- Two varaibles can be varied as per your specific case:
    - var "threshold" (depends on amount of change between two frames) can be 
        - decreased if getting False Positives(getting unnecessary images).
        - increased if missing True Positives(missing usefull images).
    - var "skipBy" (depends on speed of slides) can be
        - decreased if missing True Positives(missing usefull images).
        - increased if getting False Positives(getting unnecessary images).

## Steps
- Install required libraries using
    - ` pip install -r requirements.txt`
    - If something else is missing, please download it as well using help of stackoverflow ;)
- Script Run Command
    - `python script.py Sample.mp4`
    - replace "Sample.mp4" with <your file's name>
    - it will create a PDF named <your file's name>.pdf
