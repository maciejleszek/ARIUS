const API_BASE_URL = "http://localhost:5000/api";

// Helper function for making API requests
async function apiRequest(endpoint, method = "GET", body = null, token = null) {
    const headers = {
        "Content-Type": "application/json",
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
        method,
        headers,
        body: body ? JSON.stringify(body) : null,
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || "Something went wrong");
    }

    return response.json();
}

// Authentication
export async function register(userData) {
    return apiRequest("auth/register", "POST", userData);
}

export async function login(credentials) {
    return apiRequest("auth/login", "POST", credentials);
}

// Stamps
export async function getStamps() {
    return apiRequest("stamps", "GET");
}

export async function getStampDetails(stampId) {
    return apiRequest(`stamps/${stampId}`, "GET");
}

// Cart
export async function addToCart(stampId, token) {
    return apiRequest("cart/add", "POST", { stampId }, token);
}

export async function removeFromCart(stampId, token) {
    return apiRequest("cart/remove", "POST", { stampId }, token);
}