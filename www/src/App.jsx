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
      <div className='relative flex flex-row w-dvh h-dvh space-x-6 px-6'>
        <div className='flex flex-col justify-center h-full p-2 space-y-4 w-10'>
          <div className='flex flex-col space-y-4'>
            <div className='flex flex-col space-y-1'>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>M</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>Y</div>
            </div>
            <div className='flex flex-col space-y-1'>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>C</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>H</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>O</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>I</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>C</div>
              <div className='flex h-full font-bold text-7xl justify-center font-bungee'>E</div>
            </div>
          </div>

        </div>
        <div className='flex flex-col justify-between h-full p-2 bg-amber-100 space-y-4'>
          <div className='flex flex-col space-y-4'>
            <img src='/logo/base_icon.png' className='max-w-64'></img>
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
          <div className='flex flex-col max-w-64 font-medium text-4xl text-rose-800 font-protest_guerrilla'>
            <div className='flex justify-center '>"to the Biggest
            </div>
            <div className='flex justify-center'> Air Cooler</div>
            <div className='flex justify-center'>Distributor
            </div>
            <div className='flex justify-center'> of Jharkhand"</div>
          </div>
          <div className='flex flex-col justify-center space-y-1 text-rose-800 font-medium font-mono text-sm'>
            <div className='flex justify-center'>Invoice Download | Partner Login</div>
            <div className='flex justify-center'>Copyright@ mychoice, 2024</div>
          </div>

          {/* <div className='flex font-bold text-xl justify-center font-bungee'></div> */}
        </div>
        <div className='flex flex-col justify-end w-full space-y-4'>
          <div className="flex min-h-72 bg-center bg-[url('/sym.webp')]">
          {/* <img src='sym.webp' className='rounded'></img> */}
          </div>
          <div className='flex flex-col'>
            <div className='flex flex-col space-y-2'>
              <div className='flex justify-center'>Authorized Dealer</div>
              <div className='flex flex-row w-full justify-center space-x-4'>
                <div className='flex w-36 h-24'>
                  <img src='logo/haier.png'></img>
                </div>
                <div className='flex w-36 h-20'>
                  <img src='logo/havells.png'></img>
                </div>
                <div className='flex w-36 h-20'>
                  <img src='logo/lg.png'></img>
                </div>
                <div className='flex w-36 h-24'>
                  <img src='logo/samsung.png'></img>
                </div>
                <div className='flex w-36 h-24'>
                  <img src='logo/voltas.png'></img>
                </div>
                <div className='flex w-36 h-24'>
                  <img src='logo/whirlpool.png'></img>
                </div>
              </div>
            </div>
            <div className='flex flex-col space-y-2'>
              <div className='flex justify-center'>Authorized Distributor</div>
              <div className='flex flex-row w-full justify-center space-x-4'>
                <div className='flex w-36 h-20'>
                  <img src='logo/hindware.jpg' className='rounded-md'></img>
                </div>
                <div className='flex w-36 h-20'>
                  <img src='logo/bajaj.png'></img>
                </div>
                <div className='flex w-36 h-20'>
                  <img src='logo/symphony.png'></img>
                </div>
                <div className='flex w-36 h-20'>
                  <img src='logo/orient.png' className='rounded-md'></img>
                </div>
              </div>
            </div>
          </div>
          <div className='flex flex-row justify-between w-full h-54 space-x-2 p-2 bg-amber-200 bg-opacity-50 rounded-md'>
            <div className='flex w-full border-r-2 border-rose-800'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>Shop No 4, Block 1, Kalimati Road</div>
                <div className='flex justify-center'>Beside Railway City Booking</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
            <div className='flex w-full border-r-2 border-rose-800'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>Shop No 4, Block 1, Kalimati Road</div>
                <div className='flex justify-center'>Beside Railway City Booking</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
            <div className='flex w-full'>
              <div className='flex flex-col w-full justify-between space-y-1 py-4 text-rose-800 text-medium text-xl'>
                <div className='flex justify-center'>Shop No 4, Block 1, Kalimati Road</div>
                <div className='flex justify-center'>Beside Railway City Booking</div>
                <div className='flex justify-center'>Sakchi, Jamshedpur</div>
              </div>
            </div>
          </div>
        </div>
        {/* <div className={`relative flex flex-col justify-center h-screen bg-white bg-center bg-no-repeat bg-cover translate-y ease-in-out duration-1000`}>
          <div className='flex lg:flex-row flex-col h-full justify-center p-6 space-x-2'>
            <div className='flex flex-col lg:h-full h-2/3 lg:justify-center justify-end lg:w-1/3 p-5 space-y-5'>
              <div className='lg:text-7xl text-5xl text-blue-900 font-medium'>under</div>
              <div className='lg:text-7xl text-5xl text-blue-900 font-medium'>Construction</div>
              <div>Our Website is under construction for any queries please mail to constactus@mychoiceworld.in</div>
            </div>
            <div className='flex flex-col lg:h-full lg:w-2/3 h-1/3 lg:justify-center justify-start mt-10'>
              <img src='/undraw_city_life_gnpr.svg'></img>
            </div>
          </div>
          <div className='absolute bottom-0 flex w-full'>
            <InfiniteSlider></InfiniteSlider>
          </div>
        </div>
        <div className='contactus flex flex-col bg-slate-50 w-full shadow-xl rounded-xl' id='contactus'>
          <div className='flex lg:flex-row flex-col justify-between w-full space-x-4 p-2'>
            <div className='flex lg:flex-col justify-center'>
              <div className='flex h-36 w-36 lg:h-56 lg:w-56'>
                <img src="android-chrome-512x512.png"></img>
              </div>
            </div>
            <div className='flex flex-col p-2 justify-center'>
              <div>
                Shop 4, Block 4, Kalimati Road
              </div>
              <div>
                Near Balajee Hotel, Sakchi
              </div>
              <div>
                Jamshedpur, Jharkhand, India-831001
              </div>
              <div>
                mychoice_jamshedpur@rediffmail.com | 9334638328
              </div>
            </div>
            <div className='flex flex-col p-2 justify-center '>
              <div>
                67, First Floor, Birenu Trade Center
              </div>
              <div>
                Near ICICI Bank, Sakchi
              </div>
              <div>
                Jamshedpur, Jharkhand, India-831001
              </div>
              <div>
                sunilelectronic@gmail.com | 9334825936
              </div>
            </div>
            <div className='flex flex-col p-2 justify-center '>
              <div>
                B/4, Hume Pipe Nirmal Nagar
              </div>
              <div>
                Near Athiti Bhawan, Bhuiyadih
              </div>
              <div>
                Jamshedpur, Jharkhand, India-831009
              </div>
              <div>
                mychoicelectronics01@gmail.com | 7970460076
              </div>
            </div>
          </div>
          <div className='flex flex-col lg:flex-row justify-center p-2 lg:p-4'>
            <div className='flex flex-row justify-center'>
              <div>
                My Choice &nbsp; | &nbsp;
              </div>
              <div>
                20AEYPA0067P1ZB  &nbsp; | &nbsp;
              </div>
            </div>
            <div className='flex flex-row justify-center'>
              <div>
                Sunil Electronic &nbsp; | &nbsp;
              </div>
              <div>
                20AEYPA0067P1ZB
              </div>
            </div>
          </div>
        </div>
        <div className='flex flex-col'>
          <div className='flex justify-center p-4'>
            <a href='https://internal.mychoiceworld.in'>For Staff Login Please click here</a>
          </div>
          <div className='flex justify-center'>
            Copyright©2024 mychoice & Rishi Agarwal
          </div>
        </div>
        <div className='fixed top-0 flex flex-row justify-between w-full h-fit font-sans bg-opacity-100 p-1 py-4 bg-gray-50 bg-no-repeat text-blue-900'>
          <div className='flex flex-col justify-center lg:w-2/3 p-4'>
            <a href='#' className='lg:text-5xl text-2xl font-bold font-sans text-blue-900'>
              MY CHOICE ELECTRONICS
            </a>
          </div>
          <div className='hidden lg:flex flex-row space-x-2 justify-end w-2/3 px-4'>
            <div className='flex flex-col w-fit text-lg justify-center font-semibold hover:bg-blue-100 p-2 rounded-md'>
              <a href='#contactus' className=''>Store Locator</a>
            </div>
            <div className='flex flex-col w-fit text-lg justify-center font-semibold hover:bg-blue-100 p-2 rounded-md'>
              <a href='#contactus'>Contact Us</a>
            </div>
          </div>
          <div className='lg:hidden flex flex-row justify-end'>
            <div className='flex flex-col w-fit justify-center font-semibold' onClick={() => { setIsSliderOpen(!isSliderOpen) }}>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-10 text-blue-900">
                <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5M12 17.25h8.25" />
              </svg>
            </div>
          </div>
          <div className={`${isSliderOpen ? '' : 'translate-x-36'} absolute -right-0 -bottom-20 flex flex-col p-4 text-lg space-y-2 font-semibold bg-white rounded-b-lg transform transition ease-in-out delay-200`}>
            <div>
              <a href='#contactus' onClick={() => { setIsSliderOpen(!isSliderOpen) }}>Store Locator</a>
            </div>
            <div>
              <a href='#contactus' onClick={() => { setIsSliderOpen(!isSliderOpen) }}>Contact Us</a>
            </div>
          </div>
        </div> */}
      </div >
    </>
  )
}

export default App
