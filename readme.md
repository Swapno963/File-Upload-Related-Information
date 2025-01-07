# DocumentCreateView API

This API view handles two HTTP methods: `GET` for fetching all documents and `POST` for creating a new document with file upload functionality.

---

## **GET Request**

### Fetch All Documents

- **Description**: Retrieves all documents from the database.
- **Process**:

  1. Fetches all `Document` objects.
  2. Serializes the objects using `DocumentGetSerializer`.
  3. Returns the serialized data in the response.
- **Response**:

  - **Status Code**: `200 OK`
  - **Data**: A list of all documents in JSON format.

---

## **POST Request**

### Create a New Document with File Upload

- **Description**: Accepts normal data (e.g., title, content) along with a file. Saves the data into separate models and creates a relationship between them.
- **Process**:

  1. **Extract File**: The file is retrieved from `request.FILES` using `request.FILES.get('file')`.
  2. **Prepare Data**: The request data is copied to ensure immutability.
  3. **Validate Data**: `DocumentSerializer` is used to validate the normal data.
  4. **Save File**: If validation succeeds, the file is saved into the `FileUpload` model with a placeholder name (`name="name"`).
  5. **Save Document**: The main document data is saved using the serializer. The saved file is linked to the document via a foreign key (`fileUpload`).
  6. **Response**: The serialized document data is returned.
- **Response**:

  - **Status Code**:
    - `201 CREATED` on success
    - `400 BAD REQUEST` if validation fails
  - **Data**:
    - **On success**: Serialized document data in JSON format.
    - **On error**: Validation errors in JSON format.

---

## **Example Workflow**

### **POST Request** (Create a Document)

- **Input**:
  ```json
  {
    "title": "Document Title",
    "content": "This is some content",
    "file": <file_to_upload>
  }
  ```
