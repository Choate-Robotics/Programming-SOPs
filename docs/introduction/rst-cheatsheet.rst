Introduction to Writing in reStructuredText (reST)
==================================================

What is reStructuredText?
-------------------------

reStructuredText (reST) is a lightweight markup language designed for creating well-structured and easily readable documents.
It is widely used for writing documentation, especially in Python projects, and integrates seamlessly with tools like Sphinx
to generate professional-quality outputs such as HTML, PDF, and LaTeX.

reStructuredText files typically have the ``.rst`` extension, which indicates that the file contains reST-formatted content.

Key Features of reST
---------------------

- **Simple Syntax**: reST uses straightforward plain-text syntax, making it easy to learn and use.
- **Readable and Structured**: Documents written in reST are both human-readable and machine-parseable.
- **Flexible Output**: reST can be converted into multiple output formats, such as HTML, PDF, or LaTeX.
- **File Naming**: Always save your reST documents with the ``.rst`` extension to ensure compatibility with tools like Sphinx.

Basic Syntax Elements
----------------------

1. **Headings**: Use underlines or overlines with characters like ``=``, ``-``, or ``~`` to create headings.
   The length of the underline should match the length of the heading text.

   Example:

   .. code-block:: rst

      Main Heading
      ============

      Subheading
      -----------

2. **Paragraphs**: A block of text separated by a blank line is treated as a paragraph.

3. **Lists**:
   - **Unordered Lists**: Use ``-``, ``*``, or ``+`` for unordered lists.
   - **Ordered Lists**: Use numbers followed by a period (e.g., ``1.``).

   Example:

   .. code-block:: rst

      - Item 1
      - Item 2
        - Subitem 2.1
      1. Step One
      2. Step Two

4. **Inline Markup**:
   - Use ``*text*`` for emphasis (italic).
   - Use ``**text**`` for strong emphasis (bold).
   - Use ````text```` for inline code.
   - Use ````text```` to mark filenames or paths for better readability.

   Example:

   .. code-block:: rst

      The configuration file is named ``settings.py``, and you can find it in the ``/config`` directory.

5. **File Names and Paths**:
   To mark text as a filename, wrap it in double backticks (```` `` ````). This makes it clear to readers that the text represents a filename, directory, or path.

   Example:

   .. code-block:: rst

      Save your document as ``my_document.rst``.
      The main script is located in the ``/src/main.py`` file.

6. **Links**:
   - **Inline Links**: Use backticks with an underscore and include the URL.

     Example:

     .. code-block:: rst

        Visit the `Python Homepage <https://www.python.org>`_ for more information.

   - **Footnote-style Links**: Define the link separately.

     Example:

     .. code-block:: rst

        Refer to the `Sphinx Documentation`_ for setup instructions.

        .. _Sphinx Documentation: https://www.sphinx-doc.org

7. **Code Blocks**: Use ``.. code-block::`` followed by the language name to format code snippets.

   Example:

   .. code-block:: rst

      .. code-block:: python

         def hello_world():
             print("Hello, world!")

Conclusion
----------

reStructuredText provides a clear, structured, and easy-to-read syntax for creating documents. By marking filenames
and paths with double backticks, you can make your documentation clearer and more accessible to readers. Remember to save
your reST files with the ``.rst`` extension to ensure compatibility with documentation tools like Sphinx. Mastering reST
is a valuable skill for anyone working on technical writing or software development projects.
