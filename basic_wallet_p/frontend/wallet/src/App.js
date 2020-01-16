import React from "react";
import "./App.css";
import UserData from "./components/UserData"

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Wallet</h1>
        <UserData />
      </header>
    </div>
  );
}

export default App

    // class App extends Component {

    //   state = {
    //     transaction: []
    //   }

      
// useEffect(() => {
//     axios
//       .get(
//         "http://localhost:5000/chain"
//       )
//       .then(response => {
//         setData(response.data);

//         console.log(response.data);
//       })
//   }, [])
      
//     }
// export default App;


