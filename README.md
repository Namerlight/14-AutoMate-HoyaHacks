# 14 - Auto-Mate

#### HoyaHacks 2024 - Shadab Choudhury & Naren Sivakumar

<img src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/003/234/998/datas/gallery.jpg">

This repository contains the two separate codebases for the Android App Front-End of Auto-Mate and the Python FastAPI Backend.

Large sections of this code are based on the open-source release of AppAgent developed by Tencent [1]. We modify the original codebase to make it more robust and reliable, 
then build FastAPI API endpoints to connect to it.

To run this section of the code, you will need a working OpenAI API key with access to the GPT-4o model. Each step costs approximately $0.03 and each task may take anywhere from 2-3 to 20+ steps.

The android component is built using Expo and React Native. It does not communicate with the python backend can issue commands to a connected android phone with USB debugging enabled or to an emulated phone.






[1] Zhang C, Yang Z, Liu J, Han Y, Chen X, Huang Z, Fu B, Yu G. Appagent: Multimodal agents as smartphone users. arXiv preprint arXiv:2312.13771. 2023 Dec 21.
