export async function fetchScannedFixtures() {
  const response = await fetch("http://localhost:5000/scan-fixtures");
  if (!response.ok) {
    throw new Error("Failed to fetch scanned fixtures");
  }
  return response.json();
}
