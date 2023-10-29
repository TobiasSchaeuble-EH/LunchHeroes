import { supabase } from "../supabaseclient";

// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";


export const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const removeUser = () => ({
	type: REMOVE_USER,
});

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await supabase.auth.signInWithPassword({
		email: email,
		password: password,
		options: {
		  redirectTo: 'https//example.com/welcome'
		}
	})
	console.log('RESPONSE', response)

	if (response.data.user) {
		const data = response.data
		localStorage.setItem('user', data.user)
		dispatch(setUser(data));
		return data;
	} else if (response.error) {
		const data = response.error
		console.log(data)
		return data.errors;
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await supabase.auth.signOut()

	if (!response.error) {
		dispatch(removeUser());
	}
};



export default function reducer(state = initialState, action) {
	switch (action.type) {
		case SET_USER:
			return { user: action.payload };
		case REMOVE_USER:
			return { user: null };
		default:
			return state;
	}
}
