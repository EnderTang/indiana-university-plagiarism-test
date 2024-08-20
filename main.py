def has_consecutive_duplicate_words(text1, text2, min_consecutive_words=7):
    words1 = text1.split()
    words2 = text2.split()

    for i in range(len(words1) - min_consecutive_words + 1):
        subset1 = set(words1[i:i+min_consecutive_words])
        for j in range(len(words2) - min_consecutive_words + 1):
            subset2 = set(words2[j:j+min_consecutive_words])

            if subset1 == subset2:
                return True

    return False

# text here
text1 = "In a complex task such as creating a website for learning, instructors may want to support the generation of multiple solutions in learners' peer feedback. Anonymity may create a social context where learners feel freer to express varied ideas, and make the task of giving feedback less inhibited. However, teachers need to know just how anonymity impacts the learning dynamic in order to make informed choices about when anonymous configurations are appropriate in peer feedback."

text2 = "According to Howard, Barrett, and Frick (2010), in order to make appropriate choices educators must understand the ways in which hiding or showing the identity of participants can impact the interaction that takes place in peer feedback activities. Obscuring the identity of participants in peer feedback "



result = has_consecutive_duplicate_words(text1, text2)

if result:
    print("!!!7 words yes!!!")
else:
    print("no")
