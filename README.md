## Description
- It takes video as input and extract different sildes(Images) from the video.
- It Use structural_similarity to check similarity between two frames.
- Two varaibles can be varied as per your specific case:
    - var "threshold" can be 
        - decreased if getting False Positives(getting unnecessary images).
        - increased if missing True Positives(missing usefull images).
    - var "skipBy" can be
        - decreased if missing True Positives(missing usefull images).
        - increased if getting False Positives(getting unnecessary images).
