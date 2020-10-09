# wordCountWeb
Script that counts the number of words on a hardcoded website.

Highlevel algorithm
1. get html response form the hardcoded url;
2. extract the html content from that response;
3. parse the html content and store it in a List (by line);
4. split the contents of each line (by whitespace) and store them to another List;
5. test each item stored to the second list and count them only if they are an alphabet or a number.