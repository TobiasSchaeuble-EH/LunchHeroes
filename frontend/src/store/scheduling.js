const SET_MEETING = "meeting/SET_MEETING";
const REMOVE_MEETING = "session/REMOVE_MEETING";

export const setMeeting = (user) => ({
	type: SET_MEETING,
	payload: user,
});

const removeMeeting = () => ({
	type: REMOVE_MEETING,
});


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

export const getMatchedUsers = (userId) => async (dispatch) => {
    const response = await fetch(`/get_meeting_data/${userId}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    console.log(response)
    if (response.ok) {
        const data = await response;
        dispatch(setMeeting(data));
        if (data.errors) {
            return;
        }
    }
}

const initialState = {
    meeting: null
}

export default function meetingReducer(state = initialState, action) {
	switch (action.type) {
		case SET_MEETING:
            state.meeting = action.payload
			return state ;
		case REMOVE_MEETING:
			return null ;
		default:
			return state;
	}
}
