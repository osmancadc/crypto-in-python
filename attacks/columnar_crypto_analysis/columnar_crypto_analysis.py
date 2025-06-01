import natural_language_analysis as nla
import columnar_transposition as ct
import time


def main():
    encrypted_text = input("Enter text to be decrypted: ")
    start_time = time.perf_counter()

    decrypted_data = crypto_analysis(encrypted_text)

    if not decrypted_data or len(decrypted_data["keys"]) == 0:
        print("No possible decryption obtained")
    else:
        print_decrypted_data(decrypted_data)

    end_time = time.perf_counter()

    elapsed = end_time - start_time
    print(
        f"It took {elapsed}S to hack this text that was {len(encrypted_text)} letters long"
    )


def crypto_analysis(text, options=3):

    text = nla.normalize_text(text)

    print("Testing possible keys")

    candidates = []
    scores = []
    keys = []

    weights = {
        "ttr": 0.7,  # Vocabulary diversity
        "freq": 0.3,  # Letter patterns
        "words": 0.1,  # Word count bonus
    }

    for key in range(2, len(text)):
        candidate_text = ct.decrypt(text, key)

        normalized_candidate = nla.normalize_text(candidate_text)

        token_ratio = nla.type_token_ratio(normalized_candidate)
        frequency_score = nla.frequency_score(normalized_candidate)
        word_count = nla.word_count(normalized_candidate)

        if token_ratio >= 0.3:
            score = (
                weights["ttr"] * token_ratio
                + weights["freq"] * frequency_score
                + weights["words"] * word_count
            )

            candidates.append(candidate_text)
            scores.append(score)
            keys.append(key)

    if len(scores) == 0:
        return []

    return get_top_results(candidates, scores, keys, options)


def get_top_results(candidates, scores, keys, options):
    top_indexes = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[
        :options
    ]
    top_candidates = [candidates[i] for i in top_indexes]
    top_scores = [scores[i] for i in top_indexes]
    top_keys = [keys[i] for i in top_indexes]

    return {"candidates": top_candidates, "keys": top_keys, "scores": top_scores}


def print_decrypted_data(decrypted_data):
    print("\n\nDecryption finalized, Results: \n\n")
    for i in range(len(decrypted_data["keys"])):
        key = decrypted_data["keys"][i]
        candidate_text = decrypted_data["candidates"][i]
        token_ratio = decrypted_data["scores"][i]
        message = candidate_text[:100] if len(candidate_text)>100 else candidate_text
        print(f"Option {i+1}) \n Possible key: {key} \n Score: {token_ratio:.4f} \n Message: {message}...")
    print("---------------------------------------------------")


def read_file_to_string(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().replace("\n", " ")  # Replace newlines with spaces
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


if __name__ == "__main__":
    main()
