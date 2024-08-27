# SageMath environment setup
from sage.all import Integer, FiniteField, EllipticCurve, randint


def main():
    # secp256k1 parameters as per:
    # <https://en.bitcoin.it/wiki/Secp256k1>, and
    # <https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/constructor.html>
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    a4 = 0
    a6 = 7
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

    # Generator point G:
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

    # Define the secp256k1 curve
    F = FiniteField(p)
    E = EllipticCurve([F(a4), F(a6)])
    G = E(Gx, Gy)

    # Step 1: Get a random point on the curve as per BIP-341
    x = Integer(0x50929B74C1A04954B78B4B6035E97A5E078A5A0F28EC96D547BFEE9ACE803AC0)

    # Step 2: Lift x to a valid point on the curve
    H_point = E.lift_x(x)

    # Step 3: Generate a random scalar r and calculate rG
    r = randint(1, n - 1)
    rG = r * G

    # Step 4: Combine H_point with rG to create the final public key: P = H + rG
    combined_point = H_point + rG

    # Step 5: Convert to the XOnly format by taking the x-coordinate
    pubkey_xonly = combined_point.x()

    msg = "Verifiably Unspendable XOnlyPublicKey using H + rG:"
    print(msg)
    print("=" * len(msg))

    print(f"XOnlyPubkey: {hex(pubkey_xonly)}")
    print(f"r          : {hex(r)}")


if __name__ == "__main__":
    main()
