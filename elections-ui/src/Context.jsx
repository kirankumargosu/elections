import React, { useState } from "react";

export const Context = React.createContext();
export const ContextProvider = ({ children }) => {
	const [items, setItems] = useState(0);
    const [selectedParty, setSelectedParty] = useState(1);

	return (
		<Context.Provider value={{ selectedParty, setSelectedParty }}>
			{children}
		</Context.Provider>
	);
};