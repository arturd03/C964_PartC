import spamDetection
import webpage


def main():
    trained_model,  trained_feature_extraction = spamDetection.initialize()
    webpage.main(trained_model,  trained_feature_extraction)

if __name__ == "__main__":
    main()