#Text = "X-DSPAM-Confidence:    0.8475"
#extract 0.8475 from above Text

text = "X-DSPAM-Confidence:    0.8475"
aa = text.find("0")

print(float(text[aa:]))
