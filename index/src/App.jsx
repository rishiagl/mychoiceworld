import './App.css'
// import logoImage from './mychoice.png'

function App() {

  return (
    <>
      <div className='relative w-dvh'>
        <div className='fixed flex flex-row justify-between w-full h-fit lg:p-4 p-2 font-sans shadow-lg rounded-xl bg-white'>
          <div className='flex flex-col justify-center w-1/3'>
            <div className='text-xl font-bold text-rose-800'>MY CHOICE ELECTRONICS</div>
          </div>
          <div className='flex flex-row justify-end lg:space-x-4 space-x-2 w-2/3'>
            <div className='flex flex-col text-xl justify-center font-semibold'>
              <a href='#contactus'>Contact Us</a>
            </div>
            <div className='flex flex-col justify-center'>
              <div className='px-4 py-2 bg-rose-800 text-white rounded-xl text-xl'>
                <a href='/offers'>
                  Offers
                </a>
              </div>
            </div>
          </div>
        </div>
        <div className="flex pt-36 h-screen bg-center bg-no-repeat bg-cover bg-[url('/hero-1920x1080.jpg')]">

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
            <a href='https://api.mychoiceworld.in/admin'>For Staff Login Please click here</a>
          </div>
          <div className='flex justify-center'>
            Copyright©2024 mychoice & Rishi Agarwal
          </div>
        </div>
      </div>
    </>
  )
}

export default App
