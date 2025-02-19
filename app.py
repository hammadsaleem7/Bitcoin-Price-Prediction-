{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c15a33b-5155-4291-bf31-61fad09c15b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-19 16:35:15.100 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Hammad Saleem\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "import os\n",
    "\n",
    "# Load the trained LightGBM model\n",
    "MODEL_PATH = \"Light Gradient Boosting Machine.pkl\"\n",
    "\n",
    "if os.path.exists(MODEL_PATH):\n",
    "    with open(MODEL_PATH, \"rb\") as f:\n",
    "        model = pickle.load(f)\n",
    "else:\n",
    "    model = None\n",
    "    st.error(\"Model file not found. Please upload a valid .pkl model file.\")\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"LightGBM Model Prediction App\")\n",
    "st.write(\"Enter the required features to get a prediction.\")\n",
    "\n",
    "# Example input fields (Modify based on your model's expected features)\n",
    "feature1 = st.number_input(\"Feature 1\", value=0.0)\n",
    "feature2 = st.number_input(\"Feature 2\", value=0.0)\n",
    "feature3 = st.number_input(\"Feature 3\", value=0.0)\n",
    "\n",
    "# Prediction button\n",
    "if model and st.button(\"Predict\"):\n",
    "    input_data = np.array([[feature1, feature2, feature3]])  # Adjust as needed\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\"Prediction: {prediction[0]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e166fcb4-2416-4fc6-a00b-1fa58eab36dc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
