# AI Shopping Agent

## Overview

AI Shopping Agent is a multimodal AI-powered shopping assistant that allows users to search for products using either text or images. The application leverages Large Language Models (LLMs), tool calling, and database interactions to provide an intelligent shopping experience.

Users can:

* Search products using natural language queries
* Upload product images and find similar products
* View product details
* Place orders through conversational interactions
* Interact with the system through a Streamlit-based user interface

---

## Features

### Multimodal Product Search

* Supports both text and image-based product searches.
* Users can upload a product image and receive relevant product recommendations.

### AI-Powered Product Recognition

* Uses a dedicated vision model to analyze product images.
* Extracts product attributes and converts them into searchable queries.

### Conversational Shopping Assistant

* Uses a separate LLM for:

  * Product discovery
  * Product recommendations
  * Order placement
  * Customer interactions

### Tool Calling

The agent can intelligently invoke multiple tools to complete user requests, including:

* Product search
* Product retrieval
* Order placement
* Database queries

### Database Integration

* Stores product and order information in a database.
* Enables real-time product lookup and order management.

### Streamlit User Interface

* Interactive and user-friendly web application.
* Supports image uploads and conversational interactions.

---

## Architecture

### Vision Model

Responsible for:

* Image understanding
* Product identification
* Attribute extraction

Input:

* Product Image

Output:

* Product attributes
* Search query

### Shopping Agent Model

Responsible for:

* Understanding user intent
* Tool selection
* Product recommendations
* Order placement
* Response generation

Input:

* User query
* Extracted product attributes

Output:

* Product recommendations
* Order confirmations
* Conversational responses

---

## Technology Stack

### Backend

* Python

### AI & LLM Frameworks

* LangChain
* Groq LLMs

### Database

* SQLite

### Frontend

* Streamlit

### Supporting Libraries

* PIL (Image Processing)
* Base64 Encoding
* SQLAlchemy / SQLite Integration (if applicable)

---

## Project Workflow

1. User enters a text query or uploads an image.
2. The vision model analyzes uploaded images.
3. Product attributes are extracted.
4. The shopping agent selects appropriate tools.
5. Database queries are executed.
6. Relevant products are retrieved.
7. The agent generates recommendations.
8. Orders can be placed directly through the interface.

---

## Key Concepts Demonstrated

* Multimodal AI Applications
* Tool Calling
* Agentic Workflows
* Database Integration
* LLM Orchestration
* Image Understanding
* Conversational AI
* Streamlit Application Development

---

## Future Improvements

* Vector Database Integration
* RAG-based Product Retrieval
* User Authentication
* Payment Gateway Integration
* Order Tracking System
* Recommendation Engine
* Multi-Vendor Support

---

## Author

Kartik Chelawat

Python Developer | Backend Developer | AI Enthusiast
