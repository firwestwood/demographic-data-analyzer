from demographic_data_analyzer import calculate_demographic_data
import test_module

# Run the function and print the result
result = calculate_demographic_data()

# Print each item in the result dictionary for easy viewing
for key, value in result.items():
    print(f"{key}: {value}")

# Run the tests
if __name__ == "__main__":
    test_module.main()
