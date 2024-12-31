import joblib
from datetime import datetime
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


class Machine:

    def __init__(self, df: DataFrame):
        """
        Initializes the Machine class by training a Random Forest model within a pipeline.

        Parameters:
        df: DataFrame containing training data.
        """
        try:
            # Preprocessing data
            print("Preprocessing data...")
            self.label_encoder = LabelEncoder()
            df["Rarity"] = self.label_encoder.fit_transform(df["Rarity"])

            # Define target and features
            print("Defining target and feature columns...")
            self.target = df["Rarity"]
            self.features = df.drop(columns=["Rarity"])
            self.time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Split data
            print("Splitting data into training and validation sets...")
            X_train, X_val, y_train, y_val = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42
            )

            # Create a pipeline with scaling and model
            print("Setting up the pipeline...")
            self.model = Pipeline([
                ("scaler", StandardScaler()),
                ("classifier", RandomForestClassifier())
            ])

            # Train the pipeline
            print("Training Random Forest Classifier within pipeline...")
            self.model.fit(X_train, y_train)

            # Validate the model
            accuracy = self.model.score(X_val, y_val)
            print(f"Model training complete. Validation accuracy: {accuracy:.2f}")

        except KeyError as e:
            raise KeyError(f"Missing column in input DataFrame: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during initialization: {e}")

    def __call__(self, feature_basis: DataFrame):
        """
        Make predictions with the model.

        Parameters:
        feature_basis: DataFrame containing features to predict.

        Returns:
        Tuple of predictions and confidence scores.
        """
        try:
            print("Scaling input features and making predictions...")
            probabilities = self.model.predict_proba(feature_basis)
            prediction = f"Rank {int(probabilities.argmax(axis=1)[0])}"
            confidence = probabilities.max(axis=1)[0]
            return prediction, confidence
        except ValueError as e:
            raise ValueError(f"Invalid feature input: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during prediction: {e}")

    def save(self, filepath: str):
        """
        Saves the pipeline (model + scaler) and label encoder to the specified filepath.

        Parameters:
        filepath: Path to save the model.
        """
        try:
            print(f"Saving model to {filepath}...")
            joblib.dump(self, filepath)
            print(f"Model saved successfully at {filepath}.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while saving the model: {e}")

    @staticmethod
    def open(filepath: str):
        """
        Loads the saved pipeline from the specified filepath.

        Parameters:
        filepath: Path to load the model from.
        """
        try:
            print(f"Loading model from {filepath}...")
            components = joblib.load(filepath)
            print("Model loaded successfully.")
            return components
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Model file not found: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the model: {e}")

    def info(self) -> str:
        """
        Returns the initialization timestamp.

        Returns:
        A string containing the model name and timestamp.
        """
        try:
            return f"Model: Random Forest Classifier, Initialized: {self.time_stamp}"
        except Exception as e:
            raise RuntimeError(f"An error occurred while retrieving model info: {e}")
