// manage jobs like projeciton eng and scraper
// create UUIDs for jobs, and use those UUIDs for projection version
// Exposes API to admin server to start/check jobs
// Gets notified when job is done, updates data

// Job states: RUNNING, SUCCEEDED, FAILED

// Job data: Type, Version, State, Description, CreatedTS, LastUpdatedTS
// Example: Scraper, imdb-v1, FAILED, "KeyError: 'Ebert' not found.", 10:55AM 08/14/22, 11:00AM 08/14/22
// Example: Projection Engine, uuid, RUNNING, "", 10:57AM 08/14/22, 10:57AM 08/14/22