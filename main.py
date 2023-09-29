import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

print("10101010101010101010101010101010101010101010101010101010101010101010101010101")
print("10101010101010101010101010101010101010101010101010101010101010101010101010101")
print("10101010101010101010101010101010101010101010101010101010101010101010101010101")

print("111111111 11111111  !!!!!!  !!!!!!   111111111  !!!!  !!!!  !!!!!!  !!!!!!")
print("11          lll        0       0     !!         0000  1111      !       !")
print("11          010       0       0      !!         1111  0000     !       !")
print("111111111   101      0       0       111111111  0101  1010    !       !")
print("01          000     0       0        11         !!!!  !!!!   !       !")
print("11          000    0       0         !!         !!!!  !!!!  !       !")
print("11        11111111 !111111 !!!!!!    !!         !!!!00!!!! !!!!!!  !!!!!!!")

print("10101010101010101010101010101010101010101010101010101010101010101010101010101")
print("10101010101010101010101010101010101010101010101010101010101010101010101010101")
print("10101010101010101010101010101010101010101010101010101010101010101010101010101")

def fetch_word(url, word):
    try:
        res = requests.get(url + f"/{word}")
        if res.status_code == 404:
            return f"Error for {word}: Page not found"
        else:
            data = res.json()
            return f"Data for {word}: {data}, Status Code: {res.status_code}"
    except Exception as e:
        return f"Error for {word}: {str(e)}"

def main():
    # Get the URL from the user
    url = input("Enter the base URL: ")

    # List of words to fetch
    words = ["word1", "word2", "word3"]  # Add your words here

    # Set the maximum number of concurrent requests (adjust as needed)
    max_concurrent_requests = 10

    # Create a ThreadPoolExecutor with a maximum of max_concurrent_requests threads
    with ThreadPoolExecutor(max_concurrent_requests) as executor:
        # Create a list of futures (one for each word)
        futures = [executor.submit(fetch_word, url, word) for word in words]

        # Create a progress bar using tqdm
        with tqdm(total=len(words), desc="Progress") as pbar:
            for future in as_completed(futures):
                result = future.result()
                print(result, flush=True)  # Print the result (either data or error)
                pbar.update(1)  # Update the progress bar

if __name__ == "__main__":
    main()

print("SCRIPTING COMPLETE")