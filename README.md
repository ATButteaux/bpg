# bpg
Brain Password Generator

This is a heiarchical brain password generator.

Seed it (with a secret and a piece of data) and you can branch out to different categories, based on a chain of hashes from the seed.

For example, if your seed is "All my passwords are belong to me", you can have make several data keywords for, say, work passwords, home passwords, passwords for files, etc like "work", "home", "files". Each combination of seed and additional word creates a heiarchy of hashes you can traverse.

And there are many arbitrary paths you can take, buy either choosing the hash of secret+data to seed the next level, or the right/left side of the Base58 encodings, or the decimal string.

Your password may eventually be any part of the output!

Example:

**s All my passwords are belong to me**

**d work**

```
Secret:       All my passwords are belong to me
Data:         work
Encoding:     All my passwords are belong to me-work
Hash:         06f94c33aed581a72f26e8db17371b6f1c232602a14a52b8a36064608577716d
Decimal:      0659-4233-0435-8107-2526-4831-1737-1165-1223-2602
Base58:       UDvj6-39vu6-gAKrC  jekL8-oyeD7-Yx5wj
```

**sh** (Shift Hash to secret)

```
Secret:       06f94c33aed581a72f26e8db17371b6f1c232602a14a52b8a36064608577716d
Data:         *
Encoding:     06f94c33aed581a72f26e8db17371b6f1c232602a14a52b8a36064608577716d-*
Hash:         bc7da3a1d9e5876cdc68db965617e682a826fc915e5c5aacec7b5fc2a28b8e7a
Decimal:      1273-0301-3945-8762-3268-3196-5617-4682-0826-5291
Base58:       DgnmG-7kNFq-wGMVa  TJ2Jt-gCYrq-WdDAH
```

**d computer_name**

```
Secret:       06f94c33aed581a72f26e8db17371b6f1c232602a14a52b8a36064608577716d
Data:         computer_name
Encoding:     06f94c33aed581a72f26e8db17371b6f1c232602a14a52b8a36064608577716d-computer_name
Hash:         f532204221a528c3894ffe1af8b7f75fd93330d7c0f4e62a56c6a4c9a7d1c4b2
Decimal:      5532-2042-2105-2823-8945-5410-5817-5755-3933-3037
Base58:       HW9Dd-AkGsf-BBJVA  DZJKf-QTqNL-NyTsF
```

Use the right half of the Base58 encoding for the loging password
