import { useState, useEffect } from 'react';
import './App.css'
import NumberInputGroup from './NumberInputGroup';
import { InfiniteSlider } from './InfiniteSlider';

function App() {
  const [currentBgImage, setCurrentBgImage] = useState(0);
  const [submitted, setSubmitted] = useState(false);
  const [isSliderOpen, setIsSliderOpen] = useState(false);

  function changeBgImage() {
    setCurrentBgImage((currentBgImage + 1) % 4);
  }

  useEffect(() => {
    setTimeout(changeBgImage, 7000);
  }, [currentBgImage]);


  return (
    <>
      <div className='relative flex lg:flex-row flex-col w-dvh h-dvh lg:space-x-6 lg:px-6'>
        <div className='flex lg:flex-col flex-row justify-center lg:h-full p-2 lg:space-y-4 lg:w-10 w-full'>
          <div className='flex lg:flex-col lg:space-y-6 space-x-2 lg:space-x-0'>
            <div className='flex lg:flex-col lg:space-y-2'>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>M</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>Y</div>
            </div>
            <div className='flex lg:flex-col lg:space-y-2'>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>C</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>H</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>O</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>I</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>C</div>
              <div className='flex h-full font-bold text-6xl lg:text-7xl justify-center font-bungee'>E</div>
            </div>
          </div>
        </div>
        <div className='flex flex-col justify-between lg:h-full p-2 bg-amber-100 space-y-4'>
          <div className='flex flex-col space-y-4'>
            <div className='flex justify-center'>
              <img src='/logo/base_icon.png' className='max-w-64'></img>
            </div>
            <div className='flex flex-col font-bold text-lg text-rose-800'>
              <div className='flex justify-center'>
                9334638328 / 9334825936</div>
              <div className='flex justify-center'>
                contactus@mychoiceworld.in</div>
              <div className='flex justify-center'>
                Sakchi, Jamshedpur</div>
            </div>
          </div>
          <div className='flex justify-center font-bold text-3xl text-rose-800 font-serif'>
            Welcome!!</div>
          <div className='flex flex-col lg:max-w-64 font-medium text-4xl text-rose-800 font-protest_guerrilla'>
            <div className='flex justify-center '>"to the Biggest
            </div>
            <div className='flex justify-center'> Air Cooler</div>
            <div className='flex justify-center'>Distributor
            </div>
            <div className='flex justify-center'> of Jharkhand"</div>
          </div>
          <div className='flex flex-col justify-center space-y-1 text-rose-800 font-medium font-mono text-sm'>
            <div className='flex justify-center'>Invoice Download | Partner Login</div>
            {/* <div className='flex justify-center'>Copyright@ mychoice, 2024</div> */}
          </div>
        </div>
        <div className='flex flex-col justify-end w-full space-y-4'>
          <div className="flex min-h-72 bg-center bg-[url('/sym.webp')]">
          </div>
          <div className='flex flex-col space-y-4'>
            <div className='flex flex-col space-y-2'>
              <div className='flex justify-center font-medium text-rose-800 font-serif text-base'>Authorized Dealer</div>
              <div className='flex flex-row w-full justify-center space-x-4 px-2'>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/haier.png'></img>
                </div>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/havells.png'></img>
                </div>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/lg.png'></img>
                </div>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/samsung.png'></img>
                </div>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/voltas.png'></img>
                </div>
                <div className='flex flex-col justify-center w-full h-full'>
                  <img src='logo/whirlpool.png'></img>
                </div>
              </div>
            </div>
            <div className='flex flex-col lg:flex-row lg:space-x-6 space-y-2 lg:space-y-0'>
              <div className='flex flex-col lg:w-2/3 space-y-2'>
                <div className='flex justify-center font-medium text-rose-800 font-serif'>Authorized Distributor</div>
                <div className='flex flex-row w-full justify-center space-x-4 px-12'>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/hindware.jpg' className='rounded-md'></img>
                  </div>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/bajaj.png'></img>
                  </div>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/symphony.png'></img>
                  </div>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/orient.png' className='rounded-md'></img>
                  </div>
                </div>
              </div>
              <div className='flex flex-col lg:w-1/3 lg:space-y-2'>
                <div className='flex justify-center font-medium text-rose-800 font-serif'>E-Commerce Partners</div>
                <div className='flex flex-row w-full justify-center space-x-4 px-24 lg:px-6'>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/flipkart.png'></img>
                  </div>
                  <div className='flex flex-col justify-center w-full h-full'>
                    <img src='logo/amazon.png' className='flex flex-col justify-center rounded'></img>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className='flex lg:flex-row flex-col justify-between w-full h-54 space-x-2 p-2 bg-amber-200 bg-opacity-50 rounded-md'>
            <div className='flex w-full lg:border-r-2 lg:border-b-0 border-b-2 border-rose-800'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>Shop No 4, Block 1, Kalimati Road</div>
                <div className='flex justify-center'>Beside Railway City Booking</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
            <div className='flex w-full lg:border-r-2 lg:border-b-0 border-b-2 border-rose-800'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>67, First Floor, Birenu Trade Center</div>
                <div className='flex justify-center'>Pennar Road, Ammbagan</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
            <div className='flex w-full'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>B/4 Hume Pipe Nirmal Nagar</div>
                <div className='flex justify-center'>Near Athiti Bhawan, Bhuiyadih</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
          </div>
        </div>
      </div >
    </>
  )
}

export default App  