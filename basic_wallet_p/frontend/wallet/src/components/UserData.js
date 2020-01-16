import React, { useState, useEffect } from "react";
import axios from "axios";

const UserData = () => {
  const [data, setData] = useState();

  useEffect(() => {
    axios
      .get(
        "http://localhost:5000/chain"
      )
      .then(response => {
        setData(response.data);

        console.log("response", response.data);
      });
  }, []);
  console.log("data", data)
  // the [] means you only want it it to load once

  return (
    <div>
      <div className="App">
        <h2>testing userdata</h2>
        <p> {data.map(transaction => {
                return(
                    <div key={transaction.index}>
                        <h1>{transaction.chain.transactions}</h1>
                    </div>
                )
            })} 
          </p>

      </div>
    </div>
  );
};
export default UserData;