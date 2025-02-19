{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2c15a33b-5155-4291-bf31-61fad09c15b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained LightGBM model\n",
    "def load_model():\n",
    "    with open(\"Light Gradient Boosting Machine.pkl\", \"rb\") as file:\n",
    "        model = pickle.load(file)\n",
    "    return model\n",
    "\n",
    "# Initialize model\n",
    "model = load_model()\n",
    "\n",
    "# Streamlit App\n",
    "st.title(\"LightGBM Model Prediction App\")\n",
    "st.write(\"Enter the required input values to get a prediction.\")\n",
    "\n",
    "# Sample input fields (modify based on your model requirements)\n",
    "feature1 = st.number_input(\"Feature 1\", value=0.0)\n",
    "feature2 = st.number_input(\"Feature 2\", value=0.0)\n",
    "feature3 = st.number_input(\"Feature 3\", value=0.0)\n",
    "\n",
    "# Convert input into a NumPy array\n",
    "input_data = np.array([[feature1, feature2, feature3]])\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    st.write(\"### Prediction:\", prediction[0])\n"
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
