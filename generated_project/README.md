# Project Title: Simple To-Do List Web App

## Brief Description
A lightweight, client‑side to‑do list application built with plain **HTML**, **CSS**, and **JavaScript**. Users can add, complete, and delete tasks. All tasks are saved in the browser's **localStorage**, so the list persists across page reloads and browser sessions.

---

## Tech Stack
- **HTML5** – Structure of the page (`index.html`).
- **CSS3** – Styling and responsive layout (`styles.css`).
- **JavaScript (ES6)** – Core functionality, DOM manipulation, and data persistence (`script.js`).

---

## Feature List
- **Add Tasks** – Type a task into the input field and press **Enter** or click the **Add** button.
- **Mark as Complete** – Click the checkbox next to a task to toggle its completed state.
- **Delete Tasks** – Click the trash‑can icon to remove a task.
- **Persist Data** – All tasks are stored in `localStorage`; they survive page reloads and browser restarts.
- **Responsive Design** – Works on desktop, tablet, and mobile screen sizes.

---

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone <repository‑url>
   cd <repository‑folder>
   ```
2. **Open the application**
   - Locate `index.html` in the project root.
   - Open the file directly in any modern web browser (Chrome, Firefox, Edge, Safari, etc.).
   - No server or build step is required; the app runs entirely client‑side.

---

## Usage Guide
### Adding a Task
1. Click inside the input field at the top of the page.
2. Type the description of your new task.
3. Press **Enter** **or** click the **Add** button (➕).
4. The task appears in the list below.

### Completing a Task
- Click the checkbox next to a task. The text will toggle a strikethrough style to indicate completion.

### Deleting a Task
- Click the trash‑can icon (🗑️) on the right side of a task to permanently remove it.

### Data Persistence
- All tasks are automatically saved to the browser’s **localStorage** after each change.
- When you close the tab or reload the page, the list will be restored exactly as you left it.

---

## File Structure & Extensibility
```
project-root/
│
├─ index.html      # Main HTML markup – entry point of the app.
├─ styles.css      # Styling rules – modify for visual tweaks or themes.
├─ script.js       # Core JavaScript – handles UI interactions and storage.
└─ README.md       # Documentation (this file).
```
### Where to Extend
- **HTML (`index.html`)** – Add new UI elements (e.g., filters, priority tags) within the `<body>`.
- **CSS (`styles.css`)** – Create additional classes or modify existing ones to style new elements.
- **JavaScript (`script.js`)** – Implement new functionality:
  - Import or define helper functions at the top of the file.
  - Add event listeners for any new UI components.
  - Extend the `tasks` data model (currently an array of objects `{ id, text, completed }`).
  - Update the `saveTasks()` and `loadTasks()` functions if the data schema changes.

---

## Screenshots
> **[Insert screenshots here]**
- Screenshot of the empty state.
- Screenshot showing a list with completed and pending tasks.
- Screenshot on a mobile device (responsive layout).

---

*This README references all project files but does not depend on any code from them.*
