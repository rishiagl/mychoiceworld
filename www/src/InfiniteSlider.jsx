const LOGOS = [
    <div>
        <img src="/logo/lg.png"></img>
    </div>,
    <div>
        <img src="/logo/samsung.png"></img>
    </div>,
    <div>
        <img src="/logo/voltas.png"></img>
    </div>,
    <div>
        <img src="/logo/symphony.png"></img>
    </div>,
    <div>
        <img src="/logo/bajaj.png"></img>
    </div>,
    <div>
        <img src="/logo/havells.png"></img>
    </div>,
    <div>
        <img src="/logo/lloyd.png"></img>
    </div>,
    <div>
        <img src="/logo/aquagaurd.webp"></img>
    </div>,
    <div>
        <img src="/logo/sony.png"></img>
    </div>,
    <div>
        <img src="/logo/whirlpool.png"></img>
    </div>,
    <div>
        <img src="/logo/haier.png"></img>
    </div>,


];

export const InfiniteSlider = () => {
    return (
        <div className="relative m-auto w-full overflow-hidden bg-white bg-opacity-60 before:absolute before:left-0 before:top-0 before:z-[2] before:h-full before:w-[100px] before:content-[''] after:absolute after:right-0 after:top-0 after:z-[2] after:h-full after:w-[100px] after:-scale-x-100  after:content-['']">
            <div className="animate-infinite-slider flex w-[calc(250px*10)]">
                {LOGOS.map((logo, index) => (
                    <div
                        className="slide flex w-24 items-center justify-center p-2"
                        key={index}
                    >
                        {logo}
                    </div>
                ))}
                {LOGOS.map((logo, index) => (
                    <div
                        className="slide flex w-24 items-center justify-center p-2"
                        key={index}
                    >
                        {logo}
                    </div>
                ))}
            </div>
        </div>
    );
};
