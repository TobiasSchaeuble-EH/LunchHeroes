


export const addUserToScheduling = (userId) => async (dispatch) => {
    const response = await fetch(`/button_trigger/${userId}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    console.log(response)
    if (response.ok) {
        const data = await response;
        console.log(data)
        if (data.errors) {
            return;
        }
    }
}
