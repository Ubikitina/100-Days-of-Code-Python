# Day 68 Goals

- Implement user registration functionality to allow users to sign up for the website.
- Develop user login functionality for users to log in to their accounts securely.
- Implement user logout functionality for users to securely log out of their accounts.
- Establish a secure authentication system to verify the identity of registered users.
- Enable the association of data with user accounts for a personalized experience.
- Provide access to private profile pages for registered users.
- Implement a feature allowing registered users to download a top-secret Flask Programming Cheat Sheet.
- Ensure the security and confidentiality of user information during registration and authentication processes.

The website structure that we will use is simple, with a homepage featuring buttons for registration and login, leading to a secrets page after authentication.

# What is authentication?

The goal is to provide an overview of setting up authentication from scratch.

Authentication is necessary as users interact with the website, generating data like post likes or messages. Each user needs an account, created with a username and password, to associate data with them uniquely. Authentication also helps restrict access to certain areas of the website based on user status, such as paid subscriptions for premium content.

The tutorial emphasizes the importance of securing the website and progressing from basic to industry-standard security practices.

# Encryption and hashing

In this section we discuss the concept of encryption and its levels, particularly focusing on improving security for user passwords on a website.

There are **different levels of encryption** :

- **Level one encryption** : passwords are stored in plain text. This is vulnerable.
- **Level two encryption** : authentication involving encryption. The basic idea of encryption is scrambling data to make it unreadable without the proper key.

Historical context of encryption:

- The Enigma machine was used in World War II and its encryption method.
- The Caesar cipher, one of the earliest encryption methods, is introduced as a letter substitution cipher. This method is very weak, leading to the need for stronger encryption in modern times.

**Hashing** : it is a more secure alternative to encryption. Hash functions are mathematical operations that make it nearly impossible to reverse the process, ensuring the security of stored passwords. Hashing eliminates the need for an encryption key, making it more secure. The analogy of factoring numbers is used to explain the irreversibility of hashing.

**Conclusion** : Adopting hashing in authentication processes can significantly enhance the security of user passwords on a website.

# How to hack passwords

There is a common occurrence of major companies being hacked, leading to password leaks and potential vulnerabilities for users, even if they are using hashes. How?

When multiple users have the same password, even if they use different usernames, their hashed passwords will be identical. The hacker takes advantage of the fact that the same password always results in the same hash. So, they create a table where each entry consists of a hash and the corresponding password. All this processing requires high computing power with high-performance GPUs. Once the hacker gains access to a database with hashed passwords, they compare the hashed values in the database with the entries in their precomputed **hash table**. If they find a match, it means they have discovered the original password associated with that hash.

This method allows hackers to quickly identify common passwords, especially if many users have chosen the same or easily guessable passwords. The technique becomes more powerful when hackers have access to large databases from previous security breaches, giving them a substantial set of hashed passwords to analyze and create comprehensive hash tables.

**How to avoid** : The best way to avoid being hacked is to use long and complex passwords. The short passwords are more vulnerable since it is easier to guess them by using mathematical formulas.

# Salting passwords

**Salting:** In the pursuit of enhancing password security, the focus shifts to the concept of salting.

Salting involves introducing a random set of characters to the user's password before hashing it. This additional random salt, combined with the password, contributes to a more secure hash stored in the database.

The rationale behind salting lies in **mitigating vulnerabilities observed in standard hashing** methods, such as susceptibility to dictionary attacks or hash table cracks. By incorporating a unique salt for each user, even users with identical passwords will yield different hashes due to the distinct salts used during the hashing process.

**bcrypt:** To bolster security further, there is **bcrypt** , an industry-standard hashing algorithm valued for its deliberate **slowness**. Unlike MD5, which can calculate hashes at a rate of 20 billion per second, bcrypt offers significantly slower processing, with around 17,000 hashes per second even on advanced GPUs in 2019.

**Salt rounds:** Moreover, bcrypt introduces the concept of **salt rounds** , determining how many times the password undergoes salting during hashing. Increasing the salt rounds exponentially increases the time required for hashing, thus creating a scalable defense against advancements in computing power. This adaptability allows developers to adjust the number of salt rounds periodically to align with the evolving landscape of computational capabilities.

**In summary** , salting involves introducing randomness to user passwords before hashing, and bcrypt, coupled with salt rounds, emerges as a robust solution to fortify password security. The combined approach prevents easy exploitation of common passwords and offers resilience against emerging computational capabilities, ensuring a more secure authentication process for users.