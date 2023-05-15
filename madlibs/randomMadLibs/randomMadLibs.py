from sampleInputs import code, hp, hungergames,zombie
import random

if __name__ == "__main__":
    m = random.choice([code, hp, hungergames,zombie])
    m.madlib()