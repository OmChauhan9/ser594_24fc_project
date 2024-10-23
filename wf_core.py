import wf_dataprocessing
import wf_visualization

def main():
    print("Starting data processing...")
    wf_dataprocessing.main()  # Ensure this function exists in wf_dataprocessing.py

    print("Starting visualization...")
    wf_visualization.main()  # Ensure this function exists in wf_visualization.py

if __name__ == "__main__":
    main()  # This runs the main function when the script is executed
