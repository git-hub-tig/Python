try:
    print("try")
    raise Exception("hi")
    # raise RuntimeError("hi")

except Exception:
    print("in except")