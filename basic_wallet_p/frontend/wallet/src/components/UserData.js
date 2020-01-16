import React, { useState, useEffect } from "react";
import axios from "axios";

const UserData = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(
        "http://localhost:5000/chain"
      )
      .then(response => {
        setData(response.data.chain);

        console.log("response", response.data);
      });
  }, []);
  console.log("data", data)
  // the [] means you only want it it to load once

  return (
    <>
    <div>
    <h2>transaction data working!</h2>
      {data && data.map(block => {
        return(
        // console.log(block.index)
            block.transactions.map(transaction => { 
              return <h2>Receipient:{transaction.recipient} Amount:{transaction.amount}Timestamp:{block.timestamp}</h2>

            }))
            })} 
       
      </div>
    </>
  );
};
export default UserData;