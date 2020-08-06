text = "X-DSPAM-Confidence:    0.8475"
c=text.find('0')
print(float(text[c:]))