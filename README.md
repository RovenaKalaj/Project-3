# Project-3
# Auction Market Place for NFTs
![Alt text](nft_project.png)
## Table of Contents
* [Description](#description)
* [Goals](#project-goals)
* [Data Collection and Preparation](#data-collection-and-preparation)
* [Development and Technologies](#development-and-technologies)
* [Instructions](#instructions)
* [Outcome And Summary](#outcome-and-summary)




## Description
---
In this project, I aim to create an NFT marketplace decentralized application (dapp) for the auction of digital assets using smart contracts, solidity, and streamlit.

## Goals
---



In recent years, there has been an ever-increasing interest in NFTs - As an example, one NFT which was just an image of a column written in the New York Times sold for $560,000 in a matter of days. Observing such keen interest in the demand and sale of NFTs as well as the expanding market for digital assets, I felt it would be a great idea to launch my own  NFT dApp Auction Marketplace. 

![Alt text](nft.png)

My NFT dApp's goal is to support local and emerging artists and provide them with a fast and efficient FinTech platform to register their work and sell them through an auction-based marketplace allowing them to connect with collectors all over the world through a decentralized network.

 NFT dApp auction marketplace provides:
1. A platform that connects artists and collectors through blockchain technology with complete transparency. It holds an asset/token/deed that is to be auctioned using ERC721 standards.
2. Ability to place bids in auctions, over a decentralized network with the following functions and features: </br>
>
        - the ability to participate in an English auction whereby bid prices keep increasing over the duration of the auction.
        - the ability to monitor the auction process (start bid, bid price, the highest bidder, etc.)
        - the ability to view the frequency of each bidder
        - safe and secure transfer of NFT ownership upon auction completion
        - safe and secure transfer of funds upon auction completion
        - refund of funds to bidders that did not get not lucky
3. Use of Polygon Network provides the users with a method that is lower in cost and more efficient (faster) as compared to transacting directly over the Ethereum Network (Polygon is essentially a "scaling solution" that aims to address the inefficiencies of transacting with the high demand Ethereum network - it groups multiple transactions into a single block before committing to the main Ethereum network)
4. Works with digital assets stored over an established and secure file storage system (IPFS - Pinata)
5. Our NFT dApp does not charge any fees or retain any of the profits from the NFT sales hence providing a free-of-cost platform for the artists. As opposed to OpenSea, which charges a chunky one-time registration fee to list each NFT as well as recurring fees.


## Data Collection and Preparation
---

In order to test and demo my application I need to have an inventory of digital artwork. I created some custom ones using Photoshop. In order to generate the IPFS links for the custom artwork, I utilized Pinata. 



## Development and Technologies
---

 NFT dApp marketplace is build using the following technologies: 
* Solidity (smart contracts)
* Remix IDE
* Streamlit (frontend)
* MetaMask (wallet)
* Decentralized Blockchain Network (Polygon TestNet/Ganache)
* Xbox GameBar/Quicktime Player (Demo Video)
* ChainLink (new technology/library - not covered in class)
* Pinata
* Photoshop
* Python
* VSCode

### Libraries Used
* os
* json
* requests
* eth_account
* eth_typing
* web3
* pathlib
* dotenv
* streamlit
* dataclasses
* typing
* chainlink (AggregatorV3Interface)
* openzeppelin (ERC721, ERC721URIStorage, Ownable, Counters)



## Instructions - Environment Preparation
---

### Add Polygon Mumbai Testnet to MetaMask steps:

1. Open MetaMask and select `Settings`
2. Select `Networks`
3. Select `Add Network`
4. Enter Network Name `Matic-Mumbai`
5. Enter New RPC URL `https://rpc-mumbai.maticvigil.com/`
6. Enter Chain ID `80001`
7. Enter Currency Symbol `MATIC`
8. Enter Block Explorer URL `https://mumbai.polygonscan.com/`
9. Add MATIC to accounts via https://faucet.polygon.technology/


### Obtain RPC Server Address

1. Option 1 - Polygon Mumbai Test - Intended Project Blockchain - Create account with https://rpc.maticvigil.com/ and create dapp RPC link for Mumbai Testnet.
2. Option 2 - Ganache - Backup Project Blockchain - Simply copy RPC Server from Ganache UI.

### Load Keys In .env File

1. Load `PINATA_API_KEY` and `PINATA_SECRET_API_KEY` to .env file for IPFS Hashing and Storage
2. Load `WEB3_PROVIDER_URI` with RPC Server address.
3. Load `SMART_CONTRACT_ADDRESS` according to streamlit dapp. NFTRegistry dapp requires the `NFTRegistry.sol` contract address when deployed from Remix. Auction dapp requires `auction.sol` contract address when deployed from Remix.
4. Load wallet's `MNEMONIC` seed phrase.

### Remix Steps:

To run the application, clone the code from this GitHub repository.

1. Compile the `auction.sol` to ensure it compiles without any errors. 

2. Compile the `AuctionRegistry.sol` to ensure it is compiled successfully.

3. Prior to deployment, ensure your MetaMask/wallet is connected and the corresponding item (Injected Web3 for Remix IDE) is selected.

4. Deploy the `auction.sol` and check the deployed contracts to ensure it is there. Copy the address as it would be required for the next step.

5. Add the `auction.sol` contract address to the Deploy the AuctionRegistry.sol and proceed to deploy the AuctionRegistry.sol

6. In `AuctionRegistry.sol` deployed contract, use the address of the Auction contract in the SetApprovalForAll input field and a value of true to ensure the NFT that will be registered can participate in the Auction.

7. In `AuctionRegistry.sol` deployed contract, use the registerNFT fields to provide an address ownner and key NFT details and register it for the Auction.

8. To proceed with the auction process on the registered NFT, please follow the steps demonstrated in the Auction Demo (see Videos Demos section).



### streamlit dapp

1. Copy deployed `AuctionRegistry.sol` contract address to SMART_CONTRACT_ADDRESS key in .env file in location of AuctionRegistry dapp. Do the same for `auction.sol`, but in separate .env file in location of Auction dapp. Locations for each captured in below steps
2. Open command line interface terminal
3. For NFTRegistry dapp, navigate to location Project-3/Final/Streamlit_for_registry, then input command `streamlit run app.py`



## Outcome and Summary

Though I aimed to achieve a minimum viable product (MVP) within 2 weeks, I was not fully successful in working out every bug I have encountered. Below is a list of known bugs in the current version of My NFT dApp's NFT Auction House and some areas to consider for optimizations:

### Optimization and Debugging Opportunities

1. **Polygon (MATIC) Mumbai Testnet** - In Remix, there are no issues deploying to Polygon's Mumbai testnet. However, when running dapp via streamlit, I was unable to successfully load address accounts. Thus, more time would be needed to resolve the dapps operability with Polygon. In order to circumvent the issue with the project as is, loading Ethereum's Ganache testnet is a sufficient solution. Please note, obtaining a MATIC/USD price feed via the `getLatestPrice` call function is only possible when connected to Polygon's Mumbai testnet. Otherwise, this function is not operable when connected to Ganache.
2. **Interoperability of streamlit dapps** - The current state of the project has 2 separate dapps. One for registering NFTs only possible via the auction owner and then another one to place bids on NFTs that are registered. However, A programmatic mechanism has not been sufficiently worked out to connect operability of boths dapps seamlessly. Alternatively, considerations may be made to consolidate the dapps into a single frontend platform.
___


## Contributor
---
Rovena




## References and Resources
---
[NFT Sales](https://www.nytimes.com/2021/03/26/technology/nft-sale.html)</br>
[NFT Sale Volumes](https://thedefiant.io/nft-sales-boom-past-100m-in-30-days/)</br>
[Gas-Free NFT IPFS](https://opensea.io/blog/announcements/decentralizing-nft-metadata-on-opensea/)</br>
[OpenSea Fees](https://support.opensea.io/hc/en-us/articles/1500006315941-What-are-gas-fees-on-Ethereum-)</br>
[dAPP Auction](https://github.com/sbwengineer/auction-dapp-solidity-vue)</br>
[What is Polygon?](https://www.wealthsimple.com/en-ca/learn/what-is-polygon?utm_term=&matchtype=&campaign=16685794737&adgroup=138618658447&gclid=CjwKCAjwx46TBhBhEiwArA_DjH4oks3iZWEumuZnRH1iTbVFVlwNUI9OVcZhZeqe6JPyX30xUS4fChoCJxQQAvD_BwE#the_problem_with_ethereum)</br>
[NFT Auction](https://github.com/techwithtim/Solidity-NFT-Auction)</br>
[NFT Marketplace](https://betterprogramming.pub/solidity-contracts-for-an-nft-marketplace-5a706bb94486)</br>
[NFT Marketplace](https://betterprogramming.pub/solidity-contracts-for-an-nft-marketplace-5a706bb94486)</br>
[ChainLink Price Feed](https://docs.chain.link/docs/get-the-latest-price/)</br>
[OpenZeppelin Contracts Wizard](https://docs.openzeppelin.com/contracts/4.x/wizard) </br>
[OpenZeppelin ERC721 Docs](https://docs.openzeppelin.com/contracts/3.x/api/token/erc721#IERC721-setApprovalForAll-address-bool-)</br>



Copyright © 2023. All Rights Reserved.
